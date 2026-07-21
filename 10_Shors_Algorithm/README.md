# Shor's Algorithm with Qiskit

Implementation of **Shor's Algorithm** — one of the most famous quantum algorithms. Shor's Algorithm uses **Quantum Phase Estimation (QPE)** to determine the period of a modular arithmetic function, allowing a quantum computer to efficiently factor integers. This algorithm demonstrated that quantum computers can solve the integer factorization problem exponentially faster than the best known classical algorithms.

## What's here

- `ShorsAlgorithm.py` — implements an educational version of Shor's Algorithm for factoring **15** using Quantum Phase Estimation, controlled modular multiplication, the Inverse Quantum Fourier Transform (IQFT), and classical post-processing.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python ShorsAlgorithm.py
```

The program factors

```text
15
```

using the modular multiplication operator

\[
U|y\rangle = |2y \bmod 15\rangle
\]

and estimates the phase associated with the periodic function

\[
2^x \bmod 15.
\]

## Example Output

```text
{
    '1100': 261,
    '0000': 246,
    '1000': 266,
    '0100': 251
}
```

The measured binary values correspond to the phases

```text
0000 → 0
0100 → 1/4
1000 → 1/2
1100 → 3/4
```

These phases reveal the period

```text
r = 4
```

which allows the classical portion of Shor's Algorithm to recover the factors

```text
15 = 3 × 5
```

## How it works

The algorithm begins by preparing the counting register in an equal superposition using Hadamard gates while initializing the work register to the state `|0001⟩`. Controlled modular multiplication gates implementing `a^(2^k) mod 15` encode the hidden period into the phases of the counting register.

The Inverse Quantum Fourier Transform (IQFT) converts this phase information into its binary representation. Measuring the counting register produces estimates of the phase, which are then processed using continued fractions to recover the period `r`. Finally, the classical post-processing step computes:

```text
gcd(a^(r/2) - 1, N)
```

and

```text
gcd(a^(r/2) + 1, N)
```

yielding the non-trivial factors of the integer being factored. For this implementation:

```text
N = 15
a = 2
r = 4
```

which gives:

```text
gcd(2² - 1, 15) = gcd(3, 15) = 3
gcd(2² + 1, 15) = gcd(5, 15) = 5
```

Therefore,

```text
15 = 3 × 5
```

Shor's Algorithm is one of the landmark achievements in quantum computing. It combines Quantum Phase Estimation, modular arithmetic, the Quantum Fourier Transform, and classical number theory to solve the integer factorization problem far more efficiently than any known classical algorithm, forming one of the strongest demonstrations of quantum computational advantage.