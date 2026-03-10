# 🧪 Molecular Property Prediction

Bio-AutoResearch framework for molecular property prediction using Graph Neural Networks.

## 🎯 Overview

This sub-project implements autonomous research on predicting molecular properties from graph structures using GNNs (Graph Neural Networks).

## 📁 Files

```
molecular/
├── prepare_mol.py    # Molecular graph data generator
├── train.py          # GNN model + training loop (agent modifies)
├── program.md        # Agent research instructions
└── README.md         # This file
```

## 🚀 Quick Start

```bash
# Install dependencies
uv sync

# Run baseline experiment
uv run python train.py
```

**Expected output**:
```
🧪 Bio-AutoResearch: 分子性质预测
📱 设备: cuda
✅ 训练集: 5000 分子
✅ 验证集: 500 分子
📈 模型参数量: 14,977
🏆 最佳验证MSE: ~18.09
```

## 🔬 Technical Details

### Model Architecture

**MolecularGNN** - Message Passing Neural Network
- **Input**: Molecular graphs (atom features + adjacency matrix)
- **Architecture**:
  - Node projection layer
  - 3 message passing layers with residual connections
  - Graph-level pooling (mean aggregation)
  - Output projection for regression
- **Parameters**: ~15K
- **Training**: AdamW optimizer, MSE loss

### Data

**Simplified Molecular Dataset**
- **Training**: 5,000 random molecular graphs
- **Validation**: 500 graphs
- **Features**:
  - 5 atom types (H, C, N, O, F)
  - Up to 29 atoms per molecule
  - Random bonding patterns
  - Heuristic property targets

### Baseline Results

```
Metric                  Value
─────────────────────────────
Train Steps             318,710
Time Budget              5 minutes
Initial Val MSE           190.43
Best Val MSE               18.09
Final Val MSE              20.10
GPU                 ✓ (CUDA)
```

## 🤖 Autonomous Research

### How it Works

1. **AI Agent** reads `program.md` for instructions
2. **Modifies** `train.py` (only file agent can change)
3. **Trains** for exactly 5 minutes
4. **Evaluates** validation MSE
5. **Keeps or discards** changes based on improvement
6. **Repeats** autonomously

### Improvement Strategies

The agent can explore:
- **Architecture**: GNN depth, hidden dimensions, activation functions
- **Training**: Learning rate, batch size, optimizer type
- **Regularization**: Dropout, weight decay, batch normalization
- **Loss functions**: MSE variants, Huber loss
- **Advanced**: Edge features, attention mechanisms, pooling strategies

### Starting Agent Research

```bash
# In your AI chat interface (Claude/Codex/etc.)

"请阅读 molecular/program.md，然后开始第一个改进实验。
请说明你的假设，进行修改，并运行 train.py 验证效果。"
```

## 📊 Design Principles (from original autoresearch)

✅ **5-minute time budget** - Comparable experiments
✅ **Single file modification** - Only `train.py`
✅ **Self-contained** - Minimal dependencies
✅ **Reviewable diffs** - Clear change history
✅ **Single metric** - MSE optimization

## 🔧 Modifications from Original autoresearch

| Component | Original | Molecular |
|-----------|----------|-----------|
| **Data** | Text tokens | Molecular graphs |
| **Model** | GPT | Molecular GNN |
| **Metric** | val_bpb | val_mse |
| **Task** | Language modeling | Property prediction |

## 📈 Expected Results with Agent

Running autonomous research overnight (~100 experiments):

- 📊 **Experiment log** - All attempts and outcomes
- 🏆 **Best config** - Optimal hyperparameters found
- 💡 **Strategies** - What worked/didn't work
- 📈 **Improvement** - ~10-20% MSE reduction expected

## 🚀 Extensions

Based on this framework, you can extend to:

- **Real molecular datasets** (QM9, ChEMBL, MoleculeNet)
- **Advanced GNNs** (GAT, GraphSAGE, MPNN)
- **Multi-property prediction**
- **Molecule generation**
- **Drug discovery tasks**

## 📚 Documentation

- [Main Project README](../README.md)
- [中文文档](README_CN.md)
- [Quick Start Guide](QUICK_START.md)
- [Minimal Changes Analysis](MINIMAL_CHANGES.md)

## 🙏 References

- [karpathy/autoresearch](https://github.com/karpathy/autoresearch) - Original framework
- [PyTorch Geometric](https://pyg.org/) - GNN library
- [MoleculeNet](https://moleculenet.org/) - Molecular benchmarks

---

**Ready to start autonomous molecular research?** 🚀🧪
