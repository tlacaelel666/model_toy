
# <span style="font-family: 'Roboto', Gadget, sans-serif;">🌌QUANTUM TOY MODEL🌌</span>

## RFSC Experimental Framework

![GitHub last commit](https://img.shields.io/github/last-commit/tlacaelel666/model_toy)
![GitHub stars](https://img.shields.io/github/stars/tlacaelel666/model_toy?style=social)
![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-Apache_2.0-green)
![Theory](https://img.shields.io/badge/Theory-RFSC-purple)
![Brand](https://img.shields.io/badge/SmokApp-Software-black)

> **An interactive simulation of Systematic Causal Fragmented Reduction (RFSC) applied to a discrete topological system.**

## Overview

**Quantum Toy Model** is not just a random number generator; it is a computational exploration of the **Dynamic Information Theory (DIT)**. It models a closed quantum system where information is conserved through a topological invariant ($H=7$) and collapsed via a Golden Ratio-based operator.

This framework demonstrates how a measurement operator ($\hat{O}$) induces a deterministic bias in superposition collapse, revealing the thermodynamic cost of observation (Landauer's Principle).

## 🗝 Core Concepts

### 1. The Topological Invariant ($H=7$)
The system consists of 3 Qubits coupled as complementary dipoles. Information is never destroyed, only hidden. The sum of the **Manifest State** (measured) and the **Hidden State** (grounding) is always constant:

$$| \psi_{manifest} \rangle + | \psi_{hidden} \rangle = 7$$

| Qubit | Spin Up (Manifest) | Spin Down (Hidden) | Sum ($H$) |
| :---: | :---: | :---: | :---: |
| **Q1** | $a (1)$ | $y (6)$ | **7** |
| **Q2** | $b (2)$ | $e (5)$ | **7** |
| **Q3** | $c (3)$ | $d (4)$ | **7** |

## 2. The Golden Operator ($\hat{O}$)
Unlike standard random collapse, this model applies a custom angular projection operator based on the Golden Ratio ($\phi \approx 1.618$) and Parity ($n$):

$$\hat{O}_n = \cos(\pi n) \cdot \cos(\pi \phi n)$$

This creates a "Laminar Flow" of probability, resulting in a distinct bias (approx **88% vs 12%**) rather than maximum entropy (50/50), simulating a noise-resistant quantum channel. Manifest: 88.00%, Hidden: 12.00% (normalization in 1-6 subset) 

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- NumPy

### Installation

```
```
### Clone the repository
git clone [https://github.com/tlacaelel666/model_toy.git](https://github.com/tlacaelel666/model_toy.git)

### Navigate to the directory
cd model_toy

### Install dependencies (if applicable)
pip install -r requirements.txt

### Run toy model
python3 -m model_toy

### Output
``` 
==================================================
  QUANTUM TOY MODEL - Interactive
==================================================

Initial state: 3 qubits in superposition |ψ⟩
Sum of all states: 1+2+3+4+5+6 = 21
Operator Ô: cos(πn) * cos(πφn)

Press ENTER to measure (or 'q' to quit):(press enter)-> 

==================================================
  QUANTUM MEASUREMENT (Operator Ô)
==================================================

Operator Ô applied to superposition |ψ⟩
  P(|0⟩) = 0.8839
  P(|1⟩) = 0.1161
  → Collapsed to: |1⟩

Qubit measured: qubit_3
State: d (value=1)
Hidden state: c
H = 4 + 3 = 7

New state 4 measured. ACCUMULATING phase.
Golden Phase Accumulator: 0.0874
Accumulator Bar: [==========================                        ] # phase progretion

Press ENTER to measure (or 'q' to quit): 

```
