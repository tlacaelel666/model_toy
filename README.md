
# <span style="font-family: 'Roboto', Gadget, sans-serif;">QUANTUM TOY MODEL</span>

concepto de un modelado cuantico de información de uso experimental

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue)
![License](https://img.shields.io/badge/Apache-2.0-green)
![License](https://img.shields.io/badge/SmokApp-Software-black)
![GitHub last commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPOSITORY)
![GitHub stars](https://img.shields.io/github/stars/tlacaelel666/model_toy?style=social)


## Descripción

Este proyecto es un modelo de juguete interactivo para simular mediciones cuánticas en un sistema simple de 3 qubits.

El modelo simula la medición de un sistema cuántico en superposición, donde al aplicar un operador de medición (Ô), el sistema colapsa a un estado medido y revela un estado complementario oculto. La suma de los valores de los estados medido y oculto siempre es 7.

## Cómo ejecutar

1.  Clona este repositorio:
    cd model toy
    git clone https://github.com/tlacaelel666/model_toy.git

    python3 -m model_toy

# Quantum Toy Model

A discrete quantum system with 3 qubits as complementary pairs, demonstrating measurement-induced collapse and operator-driven state selection.

## Quick Start
```bash
git clone https://github.com/tlacaelel666/model_toy.git
cd model_toy
pip install -r requirements.txt
python -m model_toy
```

## What is this?

**3 Qubits as complementary pairs:**
- Qubit 1: a(1) ↔ y(6) → sum = 7
- Qubit 2: b(2) ↔ e(5) → sum = 7
- Qubit 3: c(3) ↔ d(4) → sum = 7

**Measurement:** Collapses one qubit to |0⟩ or |1⟩, hiding complementary state

**Operator Ô:** Governs measurement: `Ô_n = cos(πn) × cos(πφn)`

## How it works
```
Initial: All 3 qubits in superposition |ψ⟩
         Sum of all states = 21

Measure: Apply Ô operator → collapse one qubit
         State_measured + State_hidden = 7
         Other 2 qubits remain |ψ⟩

Result:  H = measured + hidden = 7
         h + H = 0 + 7 = 7 (energy conservation)
```

## Run Examples
```bash
# Interactive CLI
python -m model_toy

# Run tests (coming soon)
pytest tests/
```

## Project Structure
```
model_toy/
├── __init__.py
├── model_toy.py          # Core logic
├── operators.py          # Ô operator (to be extracted)
├── requirements.txt
├── tests/
│   ├── __init__.py
│   └── test_toy_model.py
└── README.md
```

## Theory

See `docs/THEORY.md` for mathematical formalism.

## Limitations

- Classical simulation (not actual quantum)
- Single qubit measurement at a time
- Simplified noise model
- No experimental validation

## For Recruiters

This demonstrates:
- Discrete quantum logic implementation
- Python scientific computing
- Clean code structure
- Mathematical modeling

---

**Status:** Research exploration
**License:** Apache 2.o
```

**2. Crea `requirements.txt`:**
```
numpy>=1.20.0
pytest>=6.0.0
