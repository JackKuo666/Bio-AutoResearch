# 🧪 Bio-AutoResearch

Bio-science adaptation of [karpathy/autoresearch](https://github.com/karpathy/autoresearch) - AI agents running autonomous research on molecular property prediction.

## 🎯 Core Concept

**AI Autonomous Research Loop**: Agent modifies code → trains for 5 minutes → evaluates MSE → keeps/discards → repeats

Adapts autoresearch from LLM training to **molecular property prediction** domain.

## 📁 Project Structure

```
bio_autoresearch/
├── prepare_mol.py    # Data preparation (fixed, agent does not modify)
├── train.py          # Model + training (agent modifies this file)
├── program.md        # Agent instructions (you modify this file)
├── pyproject.toml    # Dependency management
└── README.md         # This file
```

## 🚀 Quick Start

### 1. Install Dependencies
```bash
# Using uv (recommended)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync

# Or using pip
pip install torch numpy
```

### 2. Run Baseline Experiment
```bash
python train.py
```

This runs a 5-minute baseline training and outputs MSE results.

### 3. Launch AI Agent Research
In your AI chat interface (Claude/Codex/etc.):
1. Upload this project folder
2. Guide the agent to read `program.md`
3. Let the agent start autonomous experimentation

Example prompt:
```
Please read program.md and start the first improvement experiment.
Explain your hypothesis, make modifications, and run train.py to verify results.
```

## 🔬 Minimal Modifications

Compared to the original autoresearch, we **only modified 3 core components**:

### 1️⃣ Data Layer (`prepare_mol.py`)
- **Original**: Text tokenizer and data loader
- **Now**: Molecular graph data generator
- **Key**: Simplified molecular dataset (random graphs + heuristic targets)

### 2️⃣ Model Layer (`train.py`)
- **Original**: GPT language model
- **Now**: Molecular GNN (Graph Neural Network)
- **Key**: Message passing mechanism → graph-level representation → property prediction

### 3️⃣ Agent Instructions (`program.md`)
- **Original**: LLM training optimization suggestions
- **Now**: Molecular property prediction improvement directions
- **Key**: GNN architectures, graph learning techniques, loss function design

## 📊 Evaluation Metrics

| Original autoresearch | Bio-autoresearch |
|----------------------|------------------|
| val_bpb (bits per byte) | val_mse (mean squared error) |
| Lower is better | Lower is better |
| Measures language modeling | Measures molecular property prediction |

## 🎨 Design Principles (Preserved)

✅ **5-minute time budget** - All experiments run for same duration
✅ **Single file modification** - Agent only modifies train.py
✅ **Self-contained** - Minimal external dependencies
✅ **Reviewable diffs** - Every change clearly traceable
✅ **Single metric** - MSE as sole optimization target

## 🔮 Extension Directions

Based on this framework, easily extend to other bio domains:

### Protein Engineering
- Modify data: Protein sequences → structures
- Modify model: Transformer/ESM
- Modify metric: Stability/binding energy

### Genomics
- Modify data: DNA sequences → expression data
- Modify model: CNN/Attention
- Modify metric: Classification accuracy

### Medical Imaging
- Modify data: Image data
- Modify model: U-Net/ViT
- Modify metric: Dice coefficient/IoU

## 📝 Expected Results

After running overnight (~100 experiments), you will gain:
- 📈 Experiment history log
- 🏆 Best model configuration
- 💡 Effective improvement strategies
- 📊 Performance improvement curve

## 📚 Documentation

- `README_CN.md` - [中文文档](README_CN.md) (Chinese version)
- `QUICK_START.md` - Quick start guide with detailed comparisons
- `MINIMAL_CHANGES.md` - Minimal change analysis document

## 🙏 Acknowledgments

- [Andrej Karpathy](https://github.com/karpathy) - Original autoresearch concept
- [PyTorch Geometric](https://pyg.org/) - Graph neural network inspiration

## 📄 License

MIT License

---

**Ready? Let AI start autonomous bio research!** 🚀🧬
