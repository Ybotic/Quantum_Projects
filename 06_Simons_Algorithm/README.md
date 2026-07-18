# Simon's Algorithm with Qiskit

Implementation of Simon's Algorithm — discovering a hidden binary string using quantum superposition, interference, and repeated oracle queries, demonstrating one of the earliest examples of an exponential quantum speedup.

## What's here

- `simons_algorithm.py` — implements Simon's Algorithm: constructs an oracle for a chosen hidden binary string, prepares the quantum circuit, performs the oracle query, applies interference, and outputs measurement results satisfying Simon's promise.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python simons_algorithm.py
```

The program uses the chosen hidden string:

```text
Hidden string: 101
```

## Example Output

Circuit:

```text
(your printed circuit will appear here)
```

Measurement Results:

```text
{'000': 254, '010': 258, '101': 260, '111': 252}
```

Each measured bit string satisfies:

```text
y · s = 0 (mod 2)
```

Collecting enough independent measurement results allows the hidden string to be recovered using classical linear algebra over GF(2).

## How it works

The algorithm begins by placing the input register into an equal superposition of every possible binary string. A quantum oracle then evaluates the function on all inputs simultaneously while encoding the hidden structure of the function into the quantum state. A second layer of Hadamard gates causes quantum interference, eliminating invalid measurement outcomes and leaving only bit strings that satisfy the relation `y · s = 0 (mod 2)`.

Repeating the algorithm provides multiple independent equations involving the hidden string. These equations can then be solved using Gaussian elimination over GF(2) to recover the hidden string.

While the best known classical algorithms require exponentially many oracle queries to determine the hidden string, Simon's Algorithm requires only a polynomial number of queries, making it one of the first quantum algorithms to demonstrate an exponential advantage over classical computation.