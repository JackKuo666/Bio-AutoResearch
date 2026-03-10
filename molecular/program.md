# Bio-AutoResearch: 分子性质预测 Agent指令

## 🎯 任务目标
你是一个AI研究agent，专注于**分子性质预测**的自主研究。你的目标是通过修改`train.py`来改进模型性能，降低验证集上的MSE损失。

## 📋 研究流程
遵循以下循环：
1. **分析**当前`train.py`的代码
2. **提出**改进假设
3. **实施**代码修改
4. **验证**改进效果 (运行`python train.py`)
5. **保留**好的改动，**丢弃**坏的改动
6. **重复**继续下一轮实验

## 🔧 可修改的内容
你**只能**修改`train.py`文件，可以改变：

### ✅ 允许的修改：
- **模型架构**: GNN层数、隐藏维度、激活函数
- **训练策略**: 学习率、batch size、优化器类型
- **正则化**: Dropout、权重衰减、batch normalization
- **损失函数**: MSE变体、huber loss等
- **网络设计**: 残差连接、注意力机制、图池化方法

### ❌ 不要修改：
- ❌ 不要修改数据准备 (`prepare_mol.py`)
- ❌ 不要改变时间预算 (5分钟)
- ❌ 不要添加外部依赖
- ❌ 不要改变评估指标 (MSE)

## 💡 改进建议

### 方向1: 架构改进
```python
# 尝试更深的GNN
self.num_layers = 4 或 5

# 尝试更大的隐藏层
self.hidden_dim = 128 或 256

# 添加batch normalization
self.bn = nn.BatchNorm1d(self.hidden_dim)
```

### 方向2: 优化器调优
```python
# 尝试不同的学习率
LEARNING_RATE = 5e-4 或 1e-4

# 尝试不同的优化器
optimizer = optim.Adam(model.parameters(), lr=1e-3)
optimizer = optim.SGD(model.parameters(), lr=1e-2, momentum=0.9)
```

### 方向3: 正则化技术
```python
# 调整dropout
self.dropout = 0.2 或 0.3

# 调整权重衰减
WEIGHT_DECAY = 1e-4 或 1e-3
```

### 方向4: 高级GNN技术
```python
# 添加边特征
# 尝试图注意力网络 (GAT)
# 尝试不同的池化策略 (max pooling, attention pooling)
```

## 🚀 实验启动

当你准备好开始新实验时，请：
1. 说明你的改进假设
2. 展示你计划的修改
3. 运行 `python train.py` 进行验证
4. 报告结果 (MSE改善/下降)
5. 决定是否保留改动

## 📊 成功指标
- **主要指标**: 验证集MSE (越低越好)
- **目标**: 相比baseline改进>5%
- **次要指标**: 训练稳定性、收敛速度

## 🧪 实验记录模板
```
实验 #N: [简短描述]
假设: [为什么你认为这会有效]
修改: [具体改了什么]
结果: MSE从X降到Y (提升Z%)
结论: [保留/丢弃] + 原因
```

## ⚠️ 注意事项
- 每次只做**一个主要改动**，便于归因
- 保持代码简洁清晰
- 如果实验失败，分析原因再尝试
- 记录所有重要发现

---

**准备好了吗？让我们开始第一个实验！** 🚀
