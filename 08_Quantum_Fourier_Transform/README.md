# Quantum Fourier Transform (QFT) with Qiskit

Implementation of the Quantum Fourier Transform (QFT) — a fundamental quantum circuit that transforms quantum states into the Fourier basis. The QFT is one of the most important building blocks in quantum computing and serves as the foundation for algorithms such as Quantum Phase Estimation (QPE) and Shor's Algorithm.

## What's here

- `quantum_fourier_transform.py` — implements a 3-qubit Quantum Fourier Transform circuit, demonstrating the sequence of Hadamard gates, controlled phase rotations, and qubit swaps that make up the QFT.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python quantum_fourier_transform.py
```

The program prepares the quantum state:

```text
|001⟩
```

and applies the Quantum Fourier Transform.

## Example Output

Circuit:

```text
     ┌───┐                                ┌───┐
q_0: ┤ X ├──────────■─────────────■───────┤ H ├─X─
     └───┘          │       ┌───┐ │P(π/2) └───┘ │
q_1: ──────■────────┼───────┤ H ├─■─────────────┼─
     ┌───┐ │P(π/2)  │P(π/4) └───┘               │
q_2: ┤ H ├─■────────■───────────────────────────X─
```

## How it works

The Quantum Fourier Transform begins by preparing an input quantum state. A sequence of Hadamard gates creates superposition, while controlled phase gates encode phase information between qubits. The phase rotations decrease by powers of two (π/2, π/4, π/8, ...) because each lower-order qubit contributes half as much phase information as the previous one, matching the structure of binary fractions.

Finally, swap gates reverse the qubit order, producing the standard output ordering of the Quantum Fourier Transform.

Unlike Grover's or Simon's Algorithm, the Quantum Fourier Transform is not a complete algorithm by itself. Instead, it is a quantum transformation that converts a quantum state into the Fourier basis, allowing hidden phase and periodicity information to be extracted by larger algorithms such as Quantum Phase Estimation and Shor's Algorithm.