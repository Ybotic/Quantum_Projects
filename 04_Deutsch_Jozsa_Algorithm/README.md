# Deutsch Algorithm with Qiskit

Implementation of the Deutsch Algorithm — a foundational quantum algorithm that determines whether a black-box Boolean function is **constant** or **balanced** using only a single function evaluation, demonstrating quantum advantage over classical computation.

## What's here

- `deutsch.py` — builds and runs the Deutsch Algorithm for all four possible 1-bit Boolean functions (`constant_0`, `constant_1`, `balanced_identity`, and `balanced_not`) and measures the result.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python deutsch.py
```

## Results

### Constant 0 Oracle

The oracle always returns `0`.

```
Oracle: constant_0

     ┌───┐      ░  ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░──░─┤ H ├─░─┤M├
     ├───┤┌───┐ ░  ░ └───┘ ░ └╥┘
q_1: ┤ X ├┤ H ├─░──░───────░──╫─
     └───┘└───┘ ░  ░       ░  ║
c: 1/═════════════════════════╩═
                              0
```

Measurement Results:

```
{'0': 1000}
```

**The function is CONSTANT.**

---

### Constant 1 Oracle

The oracle always returns `1`.

```
Oracle: constant_1

     ┌───┐      ░       ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───────░─┤ H ├─░─┤M├
     ├───┤┌───┐ ░ ┌───┐ ░ └───┘ ░ └╥┘
q_1: ┤ X ├┤ H ├─░─┤ X ├─░───────░──╫─
     └───┘└───┘ ░ └───┘ ░       ░  ║
c: 1/══════════════════════════════╩═
                                   0
```

Measurement Results:

```
{'0': 1000}
```

**The function is CONSTANT.**

---

### Balanced Identity Oracle

The oracle returns the input unchanged (`f(x)=x`).

```
Oracle: balanced_identity

     ┌───┐      ░       ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───■───░─┤ H ├─░─┤M├
     ├───┤┌───┐ ░ ┌─┴─┐ ░ └───┘ ░ └╥┘
q_1: ┤ X ├┤ H ├─░─┤ X ├─░───────░──╫─
     └───┘└───┘ ░ └───┘ ░       ░  ║
c: 1/══════════════════════════════╩═
                                   0
```

Measurement Results:

```
{'1': 1000}
```

**The function is BALANCED.**

---

### Balanced NOT Oracle

The oracle returns the opposite of the input (`f(x)=¬x`).

```
Oracle: balanced_not

     ┌───┐      ░            ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───■────────░─┤ H ├─░─┤M├
     ├───┤┌───┐ ░ ┌─┴─┐┌───┐ ░ └───┘ ░ └╥┘
q_1: ┤ X ├┤ H ├─░─┤ X ├┤ X ├─░───────░──╫─
     └───┘└───┘ ░ └───┘└───┘ ░       ░  ║
c: 1/═══════════════════════════════════╩═
                                        0
```

Measurement Results:

```
{'1': 1000}
```

**The function is BALANCED.**

## How it works

The Deutsch Algorithm determines whether a hidden Boolean function is **constant** or **balanced** using only **one** oracle query.

The algorithm first prepares the input qubit in an equal superposition of both possible inputs (`0` and `1`) using a Hadamard gate. The auxiliary qubit is prepared in the state

\[
\frac{|0\rangle-|1\rangle}{\sqrt2}
\]

so that the oracle encodes its answer as a **phase** rather than changing measurable amplitudes directly.

The oracle evaluates both possible inputs simultaneously through quantum superposition. Instead of revealing the individual outputs, it introduces a phase difference whenever the function outputs `1`.

A second Hadamard gate converts this hidden phase information into a measurable computational basis state:

- Measuring **0** means the function is **constant**.
- Measuring **1** means the function is **balanced**.

Classically, determining this requires evaluating both `f(0)` and `f(1)` in the worst case. The Deutsch Algorithm achieves the same result with a **single** oracle evaluation, making it the first quantum algorithm to demonstrate a genuine quantum advantage.