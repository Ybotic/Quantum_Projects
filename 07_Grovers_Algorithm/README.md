# Grover's Algorithm with Qiskit

Implementation of Grover's Algorithm — searching for a marked item in an unsorted database using quantum superposition, phase inversion, and amplitude amplification, demonstrating the famous quadratic speedup of quantum search.

## What's here

- `grovers_algorithm.py` — implements Grover's Algorithm for a 2-qubit search space. The circuit prepares a superposition, marks the target state using a quantum oracle, applies the Grover diffusion operator, and measures the result.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python grovers_algorithm.py
```

The program searches for the marked state:

```text
11
```

## Example Output

Circuit:

```text
(your printed circuit will appear here)
```

Measurement Results:

```text
{'11': 1000}
```

The marked state is measured with very high probability after one Grover iteration.

## How it works

The algorithm begins by placing all possible states into an equal superposition using Hadamard gates. A quantum oracle then marks the target state by flipping its phase without changing its measurement probability.

Next, the Grover diffusion operator performs amplitude amplification, increasing the probability of the marked state while decreasing the probabilities of the remaining states.

For a search space of four possible states (2 qubits), a single Grover iteration is sufficient to amplify the marked state's probability to 100%, allowing it to be recovered with certainty after measurement.

Unlike a classical search, which requires checking items one by one, Grover's Algorithm finds a marked item in approximately √N oracle queries instead of N, providing a quadratic speedup for unstructured search problems.