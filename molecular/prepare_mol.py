"""
Bio-AutoResearch: 分子性质预测版本
对应原始autoresearch的prepare.py
功能: 数据准备、评估工具 (agent不修改此文件)
"""

import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader
from typing import List, Tuple
import urllib.request
import os

# ============ 固定常量 ============
DATASET_NAME = "QM9_subset"  # 简化版分子数据集
NUM_MOLECULES = 5000  # 限制数据量以加快训练
MAX_ATOMS = 29  # QM9最大原子数
NUM_ATOM_TYPES = 5  # H, C, N, O, F
TARGET_PROPERTY = "homo"  # 最高占据分子轨道能量

# 训练设置
DEVICE_BATCH_SIZE = 32  # 每GPU批次大小
EVAL_SAMPLES = 500  # 评估样本数

# ============ 简化的分子数据集 ============
class SimpleMoleculeDataset(Dataset):
    """简化版分子数据集 - 使用随机生成的图结构"""
    def __init__(self, num_samples=1000, max_atoms=20, num_atom_types=5):
        self.num_samples = num_samples
        self.max_atoms = max_atoms
        self.num_atom_types = num_atom_types

        # 生成随机分子图
        self.data = []
        for _ in range(num_samples):
            # 随机原子数量
            num_atoms = np.random.randint(5, max_atoms + 1)

            # 原子特征 (one-hot编码)
            atom_features = np.zeros((num_atoms, num_atom_types))
            atom_types = np.random.randint(0, num_atom_types, num_atoms)
            atom_features[np.arange(num_atoms), atom_types] = 1.0

            # 随机键连接 (邻接矩阵)
            adj = np.zeros((num_atoms, num_atoms))
            for i in range(num_atoms):
                for j in range(i+1, num_atoms):
                    if np.random.random() < 0.3:  # 30%概率形成键
                        adj[i, j] = adj[j, i] = 1.0

            # 简单的目标性质 (基于图结构的函数)
            target = self._compute_target(atom_features, adj)

            self.data.append({
                'atom_features': torch.FloatTensor(atom_features),
                'adj': torch.FloatTensor(adj),
                'num_atoms': num_atoms,
                'target': torch.FloatTensor([target])
            })

    def _compute_target(self, atom_features, adj):
        """计算一个简单的分子性质"""
        num_atoms = atom_features.shape[0]
        num_bonds = int(np.sum(adj) / 2)

        # 基于原子和键的简单启发式函数
        target = (num_atoms * 0.5 + num_bonds * 0.3 +
                 np.sum(atom_features) * 0.1 +
                 np.random.normal(0, 0.1))  # 添加噪声

        return target

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]
        return {
            'atom_features': item['atom_features'],
            'adj': item['adj'],
            'num_atoms': item['num_atoms'],
            'target': item['target']
        }

def collate_molecules(batch):
    """将不同大小的分子padding到批次最大值"""
    max_atoms = max([item['num_atoms'] for item in batch])

    batch_features = []
    batch_adj = []
    batch_targets = []
    batch_num_atoms = []

    for item in batch:
        num_atoms = item['num_atoms']

        # Padding
        padded_features = torch.zeros(max_atoms, item['atom_features'].shape[1])
        padded_features[:num_atoms] = item['atom_features']

        padded_adj = torch.zeros(max_atoms, max_atoms)
        padded_adj[:num_atoms, :num_atoms] = item['adj']

        batch_features.append(padded_features)
        batch_adj.append(padded_adj)
        batch_targets.append(item['target'])
        batch_num_atoms.append(num_atoms)

    return {
        'atom_features': torch.stack(batch_features),
        'adj': torch.stack(batch_adj),
        'target': torch.stack(batch_targets),
        'num_atoms': torch.LongTensor(batch_num_atoms)
    }

# ============ 数据准备 ============
def prepare_datasets():
    """准备训练和验证数据集"""
    print("🧪 准备分子数据集...")

    train_dataset = SimpleMoleculeDataset(
        num_samples=NUM_MOLECULES,
        max_atoms=MAX_ATOMS,
        num_atom_types=NUM_ATOM_TYPES
    )

    val_dataset = SimpleMoleculeDataset(
        num_samples=EVAL_SAMPLES,
        max_atoms=MAX_ATOMS,
        num_atom_types=NUM_ATOM_TYPES
    )

    print(f"✅ 训练集: {len(train_dataset)} 分子")
    print(f"✅ 验证集: {len(val_dataset)} 分子")

    return train_dataset, val_dataset

# ============ 评估函数 ============
@torch.no_grad()
def evaluate_model(model, val_dataset, device, batch_size=DEVICE_BATCH_SIZE):
    """评估模型性能"""
    model.eval()
    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        collate_fn=collate_molecules
    )

    total_loss = 0.0
    total_samples = 0

    for batch in val_loader:
        atom_features = batch['atom_features'].to(device)
        adj = batch['adj'].to(device)
        targets = batch['target'].to(device)
        num_atoms = batch['num_atoms']

        # 前向传播
        predictions = model(atom_features, adj, num_atoms)
        loss = torch.nn.functional.mse_loss(predictions, targets)

        total_loss += loss.item() * predictions.shape[0]
        total_samples += predictions.shape[0]

    model.train()
    return total_loss / total_samples

# ============ 主函数 ============
if __name__ == "__main__":
    print("=" * 50)
    print("Bio-AutoResearch: 分子性质预测")
    print("=" * 50)

    # 准备数据集
    train_dataset, val_dataset = prepare_datasets()

    # 测试数据加载
    train_loader = DataLoader(
        train_dataset,
        batch_size=4,
        shuffle=True,
        collate_fn=collate_molecules
    )

    batch = next(iter(train_loader))
    print(f"\n📊 批次形状:")
    print(f"  原子特征: {batch['atom_features'].shape}")
    print(f"  邻接矩阵: {batch['adj'].shape}")
    print(f"  目标值: {batch['target'].shape}")

    print("\n✅ 数据准备完成！")
