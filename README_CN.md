# 🔬 Bio-AutoResearch

基于 [karpathy/autoresearch](https://github.com/karpathy/autoresearch) 的生命科学自主研究框架集合。

## 🎯 核心概念

**AI自主研究循环**: Agent修改代码 → 训练5分钟 → 评估指标 → 保留/丢弃 → 重复

每个子项目将autoresearch适配到特定的生物科学领域，仅需最小修改。

## 📁 项目结构

```
Bio-AutoResearch/
├── molecular/          # 分子性质预测 (图神经网络)
│   ├── prepare_mol.py  # 数据生成器
│   ├── train.py        # GNN模型+训练
│   └── program.md      # Agent指令
├── protein/            # 蛋白质工程 (待开发)
├── genomic/            # 基因组学 (待开发)
├── imaging/            # 医学影像 (待开发)
└── README.md           # 本文件
```

## 🚀 快速开始

### 分子性质预测 (当前可用)

```bash
cd molecular
uv sync
uv run python train.py
```

**结果**: 训练图神经网络预测分子性质
- **模型**: 带消息传递的分子图神经网络
- **数据**: 随机分子图
- **指标**: Val MSE (~18.09 基线)
- **时间**: 每次实验5分钟

## 📊 可用领域

| 领域 | 状态 | 模型 | 数据类型 | 评估指标 |
|------|------|------|----------|----------|
| **分子预测** | ✅ 就绪 | GNN | 图结构 | MSE |
| **蛋白质工程** | 🚧 计划中 | Transformer/ESM | 序列 | 稳定性 |
| **基因组学** | 🚧 计划中 | CNN/Attention | DNA/RNA | 准确率 |
| **医学影像** | 🚧 计划中 | U-Net/ViT | 图像 | Dice/IoU |

## 🔬 核心设计原则

所有子项目遵循相同的极简设计：

✅ **5分钟时间预算** - 所有实验运行时间相同
✅ **单文件修改** - Agent只修改 `train.py`
✅ **自包含** - 最小外部依赖
✅ **可审查diffs** - 每次改动清晰可追踪
✅ **单一指标** - 每个领域一个优化目标

## 🎨 最小修改策略

每个领域相比原始autoresearch仅需修改**3个核心组件**：

1. **数据层** - 特定领域的数据生成器
2. **模型层** - 适当的神经网络架构
3. **Agent指令** - 特定领域的改进策略

## 📝 文档

- [分子性质预测](molecular/README_CN.md) - 当前实现的详细指南
- [README.md](README.md) - English version

## 🚀 扩展到新领域

添加新的生物领域：

1. **创建子目录**: `mkdir your_domain/`
2. **适配3个文件**:
   - `prepare_*.py` - 数据生成器
   - `train.py` - 模型架构
   - `program.md` - Agent指令
3. **保持设计** - 5分钟预算、单文件修改、单一指标

参考 [molecular/](molecular/) 作为实现示例。

## 📈 预期结果

运行自主研究一整夜 (~100次实验) 后获得：
- 📊 实验历史记录
- 🏆 最佳模型配置
- 💡 有效策略
- 📈 性能提升

## 🙏 致谢

- [Andrej Karpathy](https://github.com/karpathy) - 原始autoresearch概念
- PyTorch Geometric - 图神经网络灵感

## 📄 许可证

MIT License

---

**准备好开始自主生物研究了吗？** 选择一个领域开始吧！🧬🚀
