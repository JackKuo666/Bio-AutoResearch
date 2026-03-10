# Bio-AutoResearch 最小修改方案

## 核心概念
基于karpathy/autoresearch，最小化修改以支持生命科学研究。

## 原始架构分析
```
prepare.py → 数据准备 (固定)
train.py    → 模型+训练 (agent修改)
program.md  → agent指令 (人类修改)
```

## Bio领域最小修改清单

### 1. **数据层修改** (prepare.py)
```python
# 原始: 文本数据 → Bio数据
- 数据集选择: 分子数据/蛋白质序列/基因表达数据
- 数据格式: SMILES/FASTA/CSV → PyTorch tensors
- 评估指标: val_bpb → 生物相关指标
```

**推荐最小化起点:**
- **分子性质预测** (QM9、ChEMBL)
- **蛋白质稳定性预测** (ProteinGym、DeepMutationalScanning)
- **基因表达分类** (单细胞RNA-seq)

### 2. **模型层修改** (train.py)
```python
# 原始: GPT → 适合bio的架构
选项A: Graph Neural Network (分子)
选项B: Transformer/ESM (蛋白质/序列)
选项C: MLP (表格数据)
```

### 3. **评估指标** (train.py)
```python
# 原始: val_bpb → 生物指标
- 分类准确率/ AUROC
- 回归MSE/ RMSE
- 结合能得分
- 稳定性得分
```

### 4. **Agent指令** (program.md)
```markdown
# 原始: LLM训练指令 → Bio研究指令
- 领域知识约束 (化学合理性/生物学可行性)
- 可修改空间定义 (架构/超参数/loss设计)
```

## 推荐的最小实现路径

### **阶段1: 分子性质预测** (最简单)
```
数据集: QM9 (分子+量子化学性质)
模型: Message Passing GNN
指标: MSE (预测分子性质)
时间预算: 5分钟/实验
```

### **阶段2: 蛋白质序列分类**
```
数据集: 酶/非酶分类
模型: 1D CNN或Transformer
指标: Accuracy/AUROC
时间预算: 5分钟/实验
```

### **阶段3: 单细胞类型注释**
```
数据集: 10x Genomics单细胞数据
模型: 简单MLP/线性分类器
指标: F1-score
时间预算: 5分钟/实验
```

## 最小文件修改清单

### 必须修改:
1. ✏️ `prepare.py` - 数据加载器
2. ✏️ `train.py` - 模型架构+训练循环
3. ✏️ `program.md` - Agent指令

### 可选修改:
- ⚙️ `pyproject.toml` - 添加bio依赖 (rdkit, biopython, etc.)

## 保持不变的核心设计:
- ✅ 5分钟时间预算
- ✅ 单文件修改 (train.py)
- ✅ 自包含架构
- ✅ 可审查的diffs
- ✅ 单一优化指标

## 快速开始模板

### 选择数据集的考虑因素:
- **下载速度**: <1分钟
- **数据大小**: <1GB
- **预处理复杂度**: 简单
- **评估速度**: <10秒

### 推荐起点: **分子性质预测**
- 数据公开且标准化
- GNN架构成熟
- 评估快速且明确
- 领域影响大
