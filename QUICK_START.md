# Bio-AutoResearch: 最小修改对比

## 📋 核心修改总结

基于karpathy/autoresearch，构建bio-autoresearch的**最小化修改清单**:

### ✅ 必须修改的文件 (仅3个!)

| 文件 | 原始版本 | Bio版本 | 修改内容 |
|------|---------|---------|----------|
| `prepare.py` | 文本数据 | `prepare_mol.py` | 分子图数据生成器 |
| `train.py` | GPT模型 | GNN模型 | 图神经网络+训练循环 |
| `program.md` | LLM指令 | Bio指令 | 分子性质预测指导 |

### 🔄 保持不变的部分

| 组件 | 说明 |
|------|------|
| ⏱️ 时间预算 | 5分钟/实验 |
| 📁 单文件修改 | Agent只改train.py |
| 🎯 单一指标 | val_mse (原:val_bpb) |
| 🏗️ 自包含架构 | 无复杂依赖 |
| 📊 可审查diffs | 清晰的改动历史 |

## 🚀 快速启动 (3步)

### Step 1: 安装依赖
```bash
# 使用uv
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# 或pip
pip install torch numpy
```

### Step 2: 运行baseline
```bash
python train.py
```

预期输出:
```
🧪 Bio-AutoResearch: 分子性质预测
==================================================
📱 设备: cuda
📊 准备数据集...
🧪 准备分子数据集...
✅ 训练集: 5000 分子
✅ 验证集: 500 分子
🏗️ 创建模型...
📈 模型参数量: 12,345
🚀 开始训练...
Step 10 | Train MSE: 0.1234 | Val MSE: 0.1345
...
✅ 实验 MSE: 0.1200
```

### Step 3: 启动AI Agent
在你的AI聊天工具中:

```
请阅读program.md文件，然后开始自主研究。
请提出一个改进假设，修改train.py，然后运行验证效果。
```

## 📊 核心差异对比

### 数据层面
```python
# 原始: 文本tokens
token_ids = [1234, 5678, 9012, ...]

# Bio: 分子图
atom_features = [[1,0,0,0,0], [0,1,0,0,0], ...]  # H, C, N, O, F
adjacency_matrix = [[0,1,0], [1,0,1], [0,1,0]]   # 键连接
```

### 模型层面
```python
# 原始: GPT
class GPT(nn.Module):
    def forward(self, tokens):
        x = self.token_embedding(tokens)
        x = self.transformer_blocks(x)
        return self.lm_head(x)

# Bio: GNN
class MolecularGNN(nn.Module):
    def forward(self, atom_features, adj, num_atoms):
        x = self.node_projection(atom_features)
        for layer in self.gnn_layers:
            x = self.message_passing(x, adj)  # 图卷积
        return self.graph_readout(x)  # 图级别预测
```

### 评估层面
```python
# 原始: 语言建模困惑度
val_bpb = cross_entropy_loss / log(2)  # bits per byte

# Bio: 回归均方误差
val_mse = mean((predictions - targets)**2)
```

## 🎯 Agent工作流程

保持完全一致的研究循环:

```
┌─────────────────────────────────────────┐
│  1. Agent阅读train.py                   │
│  2. 提出改进假设                        │
│  3. 修改代码                            │
│  4. 运行python train.py (5分钟)        │
│  5. 检查MSE是否下降                     │
│  6. 决定:保留好的改动/丢弃坏的改动      │
│  7. 返回步骤1,继续下一轮实验            │
└─────────────────────────────────────────┘
```

## 💡 改进示例

### 示例1: 增加GNN深度
```python
# train.py 修改
# 原始:
self.num_layers = 3

# 改进:
self.num_layers = 5  # 更深的图网络
```

### 示例2: 调整学习率
```python
# train.py 修改
# 原始:
LEARNING_RATE = 1e-3

# 改进:
LEARNING_RATE = 5e-4  # 更小的学习率
```

### 示例3: 添加正则化
```python
# train.py 修改
# 添加dropout层
self.dropout = nn.Dropout(0.2)
```

## 🔬 预期实验结果

运行一整夜后 (~100次实验):

| 指标 | Baseline | 优化后 | 提升 |
|------|----------|--------|------|
| Val MSE | ~0.15 | ~0.12 | 20% |
| 训练稳定性 | 中等 | 良好 | ✅ |
| 收敛速度 | 慢 | 快 | ✅ |
| 最佳配置 | 默认 | 发现 | ✅ |

## 🎓 学习资源

如果你想深入理解各组件:

- **图神经网络**: [PyTorch Geometric文档](https://pyg.org/)
- **分子表示学习**: [DeepChem教程](https://deepchem.io/)
- **自主研究**: [原始autoresearch](https://github.com/karpathy/autoresearch)

## 🚀 下一步

1. ✅ 运行baseline
2. ✅ 启动第一个agent实验
3. ✅ 观察agent的改进策略
4. ✅ 积累实验结果
5. ✅ 分析最佳配置
6. ✅ 扩展到其他bio领域

---

**记住**: 核心思想保持不变，只是领域从语言建模切换到了分子性质预测！
