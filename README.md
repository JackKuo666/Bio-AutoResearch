# 🔬 Bio-AutoResearch

A collection of minimalist autonomous research frameworks for bio-science domains, inspired by [karpathy/autoresearch](https://github.com/karpathy/autoresearch).

## 🎯 Concept

**AI Autonomous Research Loop**: Agent modifies code → trains for 5 minutes → evaluates metrics → keeps/discards → repeats

Each sub-project adapts autoresearch to a specific bio-science domain with minimal modifications.

## 📁 Project Structure

```
Bio-AutoResearch/
├── molecular/          # Molecular property prediction (GNN)
│   ├── prepare_mol.py  # Data generation
│   ├── train.py        # GNN model + training
│   └── program.md      # Agent instructions
├── protein/            # Protein engineering (TODO)
├── genomic/            # Genomics (TODO)
├── imaging/            # Medical imaging (TODO)
└── README.md           # This file
```

## 🚀 Quick Start

### Molecular Property Prediction (Current)

```bash
cd molecular
uv sync
uv run python train.py
```

**Result**: Train a Graph Neural Network to predict molecular properties.
- **Model**: Molecular GNN with message passing
- **Data**: Random molecular graphs
- **Metric**: Val MSE (~18.09 baseline)
- **Time**: 5 minutes per experiment

## 📊 Available Domains

| Domain | Status | Model | Data Type | Metric |
|--------|--------|-------|-----------|--------|
| **Molecular** | ✅ Ready | GNN | Graphs | MSE |
| **Protein** | 🚧 Planned | Transformer/ESM | Sequences | Stability |
| **Genomic** | 🚧 Planned | CNN/Attention | DNA/RNA | Accuracy |
| **Imaging** | 🚧 Planned | U-Net/ViT | Images | Dice/IoU |

## 🔬 Core Design Principles

All sub-projects follow the same minimalist design:

✅ **5-minute time budget** - All experiments run for same duration
✅ **Single file modification** - Agent only modifies `train.py`
✅ **Self-contained** - Minimal external dependencies
✅ **Reviewable diffs** - Every change clearly traceable
✅ **Single metric** - One optimization target per domain

## 🎨 Minimal Modifications

Each domain requires only **3 component changes** from original autoresearch:

1. **Data Layer** - Domain-specific data generator
2. **Model Layer** - Appropriate neural architecture
3. **Agent Instructions** - Domain-specific improvement strategies

## 📝 Documentation

- [Molecular Property Prediction](molecular/README.md) - Detailed guide for current implementation
- [中文文档](README_CN.md) - Chinese version

## 🚀 Extending to New Domains

To add a new bio domain:

1. **Create subdirectory**: `mkdir your_domain/`
2. **Adapt 3 files**:
   - `prepare_*.py` - Data generator
   - `train.py` - Model architecture
   - `program.md` - Agent instructions
3. **Keep design** - 5-minute budget, single file mod, one metric

See [molecular/](molecular/) as reference implementation.

## 📈 Expected Results

Running autonomous research overnight (~100 experiments) yields:
- 📊 Experiment history
- 🏆 Best model configuration
- 💡 Effective strategies
- 📈 Performance improvements

## 🙏 Acknowledgments

- [Andrej Karpathy](https://github.com/karpathy) - Original autoresearch concept
- PyTorch Geometric - Graph neural network inspiration

## 📄 License

MIT License

---

**Ready to start autonomous bio research?** Pick a domain and begin! 🧬🚀
