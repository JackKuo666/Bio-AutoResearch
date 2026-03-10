"""
Bio-AutoResearch: 分子性质预测 - 训练脚本
⚠️ 这是AI Agent将修改的唯一文件
包含: 模型架构、优化器、训练循环
"""

import torch
import torch.nn as nn
import torch.optim as optim
import time
from prepare_mol import prepare_datasets, evaluate_model, collate_molecules
from torch.utils.data import DataLoader

# ============ 模型架构 (Agent可修改) ============
class MolecularGNN(nn.Module):
    """图神经网络用于分子性质预测"""

    def __init__(self):
        super().__init__()

        # === 模型超参数 (Agent可以修改) ===
        self.node_dim = 5  # 原子特征维度
        self.hidden_dim = 64  # 隐藏层维度
        self.num_layers = 3  # GNN层数
        self.dropout = 0.1  # Dropout率

        # === 消息传递层 ===
        self.node_projection = nn.Linear(self.node_dim, self.hidden_dim)

        self.gnn_layers = nn.ModuleList([
            nn.Linear(self.hidden_dim, self.hidden_dim)
            for _ in range(self.num_layers)
        ])

        # === 输出层 ===
        self.output_projection = nn.Sequential(
            nn.Linear(self.hidden_dim, self.hidden_dim // 2),
            nn.ReLU(),
            nn.Dropout(self.dropout),
            nn.Linear(self.hidden_dim // 2, 1)
        )

    def forward(self, atom_features, adj, num_atoms):
        """
        前向传播
        Args:
            atom_features: [batch, max_atoms, node_dim]
            adj: [batch, max_atoms, max_atoms]
            num_atoms: List[int] 每个分子的实际原子数
        """
        batch_size, max_atoms, _ = atom_features.shape

        # 初始节点投影
        x = self.node_projection(atom_features)  # [batch, max_atoms, hidden_dim]

        # 消息传递
        for i, gnn_layer in enumerate(self.gnn_layers):
            # 聚合邻居信息 (使用bmm进行批量矩阵乘法)
            # adj: [batch, max_atoms, max_atoms]
            # x: [batch, max_atoms, hidden_dim]
            messages = torch.bmm(adj, x)  # [batch, max_atoms, hidden_dim]

            # 归一化 (考虑度)
            degree = adj.sum(dim=-1, keepdim=True).clamp(min=1)  # [batch, max_atoms, 1]
            messages = messages / degree

            # 更新节点表示
            x = x + gnn_layer(messages)  # 残差连接

            if i < len(self.gnn_layers) - 1:
                x = torch.relu(x)

        # 图级别readout (平均池化)
        # 创建mask来标记有效的原子
        num_atoms_tensor = torch.tensor(num_atoms, device=x.device, dtype=torch.float)
        max_atoms_range = torch.arange(max_atoms, device=x.device).float()
        mask = (max_atoms_range.unsqueeze(0) < num_atoms_tensor.unsqueeze(1)).unsqueeze(-1)  # [batch, max_atoms, 1]

        # 应用mask并进行平均池化
        x_masked = x * mask  # [batch, max_atoms, hidden_dim]
        graph_repr = x_masked.sum(dim=1) / num_atoms_tensor.unsqueeze(1)  # [batch, hidden_dim]

        # 输出预测
        output = self.output_projection(graph_repr)  # [batch, 1]

        return output

# ============ 训练设置 (Agent可修改) ============
# 学习率和优化器
LEARNING_RATE = 1e-3
WEIGHT_DECAY = 1e-5

# 训练超参数
TOTAL_BATCH_SIZE = 128  # 总批次大小
GRADIENT_ACCUMULATION_STEPS = TOTAL_BATCH_SIZE // 32  # 梯度累积步数

# ============ 优化器设置 (Agent可修改) ============
def get_optimizer(model):
    """创建优化器 - Agent可以尝试不同的优化器"""
    optimizer = optim.AdamW(
        model.parameters(),
        lr=LEARNING_RATE,
        weight_decay=WEIGHT_DECAY
    )
    return optimizer

# ============ 训练循环 ============
def train_model(model, train_dataset, val_dataset, device, time_budget_seconds=300):
    """
    训练模型 - 运行固定时间预算
    Args:
        time_budget_seconds: 训练时间预算 (默认5分钟)
    """
    # 创建数据加载器
    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        shuffle=True,
        collate_fn=collate_molecules
    )

    # 优化器
    optimizer = get_optimizer(model)

    # 训练状态
    model.train()
    start_time = time.time()
    step = 0
    best_val_loss = float('inf')

    print(f"🚀 开始训练 (时间预算: {time_budget_seconds}秒)")
    print("=" * 50)

    while True:
        # 检查时间预算
        elapsed = time.time() - start_time
        if elapsed >= time_budget_seconds:
            print(f"\n⏱️ 时间预算用完 ({elapsed:.1f}秒)")
            break

        # 训练一个epoch
        epoch_loss = 0.0
        epoch_batches = 0

        for batch in train_loader:
            # 再次检查时间
            elapsed = time.time() - start_time
            if elapsed >= time_budget_seconds:
                break

            # 获取数据
            atom_features = batch['atom_features'].to(device)
            adj = batch['adj'].to(device)
            targets = batch['target'].to(device)
            num_atoms = batch['num_atoms']

            # 前向传播
            predictions = model(atom_features, adj, num_atoms)
            loss = torch.nn.functional.mse_loss(predictions, targets)

            # 反向传播
            loss.backward()

            # 梯度累积
            if (step + 1) % GRADIENT_ACCUMULATION_STEPS == 0:
                optimizer.step()
                optimizer.zero_grad()

            epoch_loss += loss.item()
            epoch_batches += 1
            step += 1

        # 计算平均损失
        avg_loss = epoch_loss / max(epoch_batches, 1)

        # 每10步验证一次
        if step % 10 == 0:
            val_loss = evaluate_model(model, val_dataset, device)
            print(f"Step {step} | Train MSE: {avg_loss:.4f} | Val MSE: {val_loss:.4f}")

            if val_loss < best_val_loss:
                best_val_loss = val_loss

    # 最终评估
    final_val_loss = evaluate_model(model, val_dataset, device)

    print("=" * 50)
    print(f"✅ 训练完成!")
    print(f"📊 最终验证MSE: {final_val_loss:.4f}")
    print(f"🏆 最佳验证MSE: {best_val_loss:.4f}")

    return final_val_loss

# ============ 主函数 ============
if __name__ == "__main__":
    print("🧪 Bio-AutoResearch: 分子性质预测")
    print("=" * 50)

    # 设置设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"📱 设备: {device}")

    # 准备数据
    print("\n📊 准备数据集...")
    train_dataset, val_dataset = prepare_datasets()

    # 创建模型
    print("\n🏗️ 创建模型...")
    model = MolecularGNN().to(device)

    # 计算参数量
    num_params = sum(p.numel() for p in model.parameters())
    print(f"📈 模型参数量: {num_params:,}")

    # 训练模型 (5分钟时间预算)
    print("\n🚀 开始训练...")
    final_mse = train_model(
        model=model,
        train_dataset=train_dataset,
        val_dataset=val_dataset,
        device=device,
        time_budget_seconds=300  # 5分钟
    )

    print(f"\n✅ 实验 MSE: {final_mse:.4f}")
