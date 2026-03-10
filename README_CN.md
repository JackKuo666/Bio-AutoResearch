# 🧪 Bio-AutoResearch

基于 [karpathy/autoresearch](https://github.com/karpathy/autoresearch) 的生命科学研究版本 - AI智能体在分子性质预测上的自主研究。

## 🎯 核心思想

**AI自主研究循环**: Agent修改代码 → 训练5分钟 → 评估MSE → 保留/丢弃 → 重复

将autoresearch从LLM训练迁移到**分子性质预测**领域。

## 📁 项目结构

```
bio_autoresearch/
├── prepare_mol.py    # 数据准备 (固定，agent不修改)
├── train.py          # 模型+训练 (agent修改这个文件)
├── program.md        # Agent指令 (你修改这个文件)
├── pyproject.toml    # 依赖管理
├── README.md         # 英文文档
└── README_CN.md      # 中文文档 (本文件)
```

## 🚀 快速开始

### 1. 安装依赖
```bash
# 使用uv (推荐)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# 或使用pip
pip install torch numpy
```

### 2. 运行基线实验
```bash
python train.py
```

这将运行一个5分钟的基线训练，输出MSE结果。

### 3. 启动AI Agent研究
在你的AI聊天界面 (Claude/Codex等) 中：
1. 上传此项目文件夹
2. 引导agent阅读 `program.md`
3. 让agent开始自主实验

示例提示词:
```
请阅读program.md，然后开始第一个改进实验。
请说明你的假设，进行修改，并运行train.py验证效果。
```

## 🔬 最小修改说明

相比原始autoresearch，我们**仅修改了3个核心部分**:

### 1️⃣ 数据层 (`prepare_mol.py`)
- **原始**: 文本tokenizer和数据加载器
- **现在**: 分子图数据生成器
- **关键**: 简化的分子数据集 (随机图+启发式目标)

### 2️⃣ 模型层 (`train.py`)
- **原始**: GPT语言模型
- **现在**: Molecular GNN (图神经网络)
- **关键**: 消息传递机制 → 图级别表示 → 性质预测

### 3️⃣ Agent指令 (`program.md`)
- **原始**: LLM训练优化建议
- **现在**: 分子性质预测改进方向
- **关键**: GNN架构、图学习技术、损失函数设计

## 📊 评估指标

| 原始autoresearch | Bio-autoresearch |
|-----------------|------------------|
| val_bpb (bits per byte) | val_mse (mean squared error) |
| 越低越好 | 越低越好 |
| 衡量语言建模 | 衡量分子性质预测 |

## 🎨 设计原则 (保持不变)

✅ **5分钟时间预算** - 所有实验运行时间相同
✅ **单文件修改** - Agent只修改train.py
✅ **自包含** - 最小外部依赖
✅ **可审查diffs** - 每次改动清晰可追踪
✅ **单一指标** - MSE作为唯一优化目标

## 🔮 扩展方向

基于这个框架，可以轻松扩展到其他bio领域:

### 蛋白质工程
- 修改数据: 蛋白质序列 → 结构
- 修改模型: Transformer/ESM
- 修改指标: 稳定性/结合能

### 基因组学
- 修改数据: DNA序列 → 表达数据
- 修改模型: CNN/Attention
- 修改指标: 分类准确率

### 医学影像
- 修改数据: 图像数据
- 修改模型: U-Net/ViT
- 修改指标: Dice系数/IoU

## 📝 预期结果

运行一整夜 (~100次实验) 后，你将获得:
- 📈 实验历史记录
- 🏆 最佳模型配置
- 💡 有效的改进策略
- 📊 性能提升曲线

## 📚 文档

- `README.md` - [English Version](README.md) (英文文档)
- `QUICK_START.md` - 快速开始指南（详细对比）
- `MINIMAL_CHANGES.md` - 最小修改分析文档

## 🙏 致谢

- [Andrej Karpathy](https://github.com/karpathy) - 原始autoresearch概念
- [PyTorch Geometric](https://pyg.org/) - 图神经网络灵感

## 📄 许可证

MIT License

---

**准备好了吗？让AI开始自主的生物研究吧！** 🚀🧬
