# Quantum Phase Estimation (QPE) with Qiskit

Implementation of Quantum Phase Estimation (QPE) — one of the most important algorithms in quantum computing. QPE estimates the phase (or eigenvalue) associated with an eigenstate of a unitary operator and serves as the foundation for algorithms such as Shor's Algorithm, quantum simulation, and quantum chemistry.

## What's here

- `QPE.py` — implements a 3-qubit Quantum Phase Estimation circuit using a Phase Gate as the unitary operator. The circuit demonstrates superposition, controlled unitary operations, the Inverse Quantum Fourier Transform (IQFT), and phase estimation.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python QPE.py
```

The program prepares the eigenstate:

```text
|1⟩
```

and estimates the phase of the unitary operator

```text
P(π/4)
```

whose eigenvalue is

```text
e^(iπ/4) = e^(2πi × 1/8)
```

## Example Output

```text
{'001': 1024}
```

The measured binary value

```text
001
```

corresponds to the binary fraction

```text
0.001₂ = 1/8
```

which is the correct phase of the chosen eigenstate.

## How it works

The algorithm begins by preparing the counting register in an equal superposition using Hadamard gates while initializing the eigenstate qubit to an eigenvector of the chosen unitary operator. Controlled powers of the unitary gate (\(U\), \(U^2\), \(U^4\), ...) encode the unknown phase into the amplitudes of the counting register.

The Inverse Quantum Fourier Transform (IQFT) then converts this hidden phase information into its binary representation. Measuring the counting register reveals the estimated phase with high probability. In this implementation, the estimated phase is exactly \(1/8\), producing the binary result `001`.

Quantum Phase Estimation is one of the most fundamental algorithms in quantum computing. Rather than solving a standalone problem, it acts as a powerful subroutine that enables larger algorithms such as Shor's factoring algorithm, quantum simulation, and many quantum chemistry applications.