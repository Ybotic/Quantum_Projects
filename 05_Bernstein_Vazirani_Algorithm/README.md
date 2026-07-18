# Bernstein-Vazirani Algorithm with Qiskit

Implementation of the Bernstein-Vazirani algorithm — discovering a hidden binary string using a single oracle query through superposition, phase kickback, and interference.

## What's here

- `bernstein_vazirani.py` — full Bernstein-Vazirani algorithm: lets the user choose a hidden binary string, constructs the corresponding oracle, runs the algorithm, and recovers the hidden string through measurement.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python bernstein_vazirani.py
```

The program will prompt you to choose one of the hidden strings:

```text
Choose the hidden string:
1. 000
2. 101
3. 110
4. 111
```

## Results

### Hidden String `000`

Circuit:

```
     ┌───┐      ░  ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░──░─┤ H ├─░─┤M├──────
     ├───┤      ░  ░ ├───┤ ░ └╥┘┌─┐
q_1: ┤ H ├──────░──░─┤ H ├─░──╫─┤M├───
     ├───┤      ░  ░ ├───┤ ░  ║ └╥┘┌─┐
q_2: ┤ H ├──────░──░─┤ H ├─░──╫──╫─┤M├
     ├───┤┌───┐ ░  ░ └───┘ ░  ║  ║ └╥┘
q_3: ┤ X ├┤ H ├─░──░───────░──╫──╫──╫─
     └───┘└───┘ ░  ░       ░  ║  ║  ║
c: 3/═════════════════════════╩══╩══╩═
                              0  1  2
```

Measurement Results:

```text
{'000': 1000}
```

Recovered hidden string: **000**

---

### Hidden String `101`

Circuit:

```
     ┌───┐      ░       ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───■───░─┤ H ├─░─┤M├──────
     ├───┤      ░   │   ░ ├───┤ ░ └╥┘┌─┐
q_1: ┤ H ├──────░───│───░─┤ H ├─░──╫─┤M├───
     ├───┤      ░   │   ░ ├───┤ ░  ║ └╥┘┌─┐
q_2: ┤ H ├──────░───│──■░─┤ H ├─░──╫──╫─┤M├
     ├───┤┌───┐ ░ ┌─┴─┐│ ░ └───┘ ░  ║  ║ └╥┘
q_3: ┤ X ├┤ H ├─░─┤ X ├┼─░───────░──╫──╫──╫─
     └───┘└───┘ ░ └───┘└─┴───────░──╫──╫──╫─
c: 3/════════════════════════════════╩══╩══╩═
                                     0  1  2
```

Measurement Results:

```text
{'101': 1000}
```

Recovered hidden string: **101**

---

### Hidden String `110`

Circuit:

```
     ┌───┐      ░       ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───■───░─┤ H ├─░─┤M├──────
     ├───┤      ░   │   ░ ├───┤ ░ └╥┘┌─┐
q_1: ┤ H ├──────░───│──■░─┤ H ├─░──╫─┤M├───
     ├───┤      ░   │  │ ░ ├───┤ ░  ║ └╥┘┌─┐
q_2: ┤ H ├──────░───│──│─░─┤ H ├─░──╫──╫─┤M├
     ├───┤┌───┐ ░ ┌─┴─┐└─┴┐└───┘ ░  ║  ║ └╥┘
q_3: ┤ X ├┤ H ├─░─┤ X ├──X┤──────░──╫──╫──╫─
     └───┘└───┘ ░ └───┘───┘──────░──╫──╫──╫─
c: 3/════════════════════════════════╩══╩══╩═
                                     0  1  2
```

Measurement Results:

```text
{'110': 1000}
```

Recovered hidden string: **110**

---

### Hidden String `111`

Circuit:

```
     ┌───┐      ░       ░ ┌───┐ ░ ┌─┐
q_0: ┤ H ├──────░───■───░─┤ H ├─░─┤M├──────
     ├───┤      ░   │   ░ ├───┤ ░ └╥┘┌─┐
q_1: ┤ H ├──────░───│──■░─┤ H ├─░──╫─┤M├───
     ├───┤      ░   │  │ ░ ├───┤ ░  ║ └╥┘┌─┐
q_2: ┤ H ├──────░───│──│■░─┤ H ├─░──╫──╫─┤M├
     ├───┤┌───┐ ░ ┌─┴─┐└┼┘└───┘ ░  ║  ║ └╥┘
q_3: ┤ X ├┤ H ├─░─┤ X ├─X───────░──╫──╫──╫─
     └───┘└───┘ ░ └───┘─────────░──╫──╫──╫─
c: 3/════════════════════════════════╩══╩══╩═
                                     0  1  2
```

Measurement Results:

```text
{'111': 1000}
```

Recovered hidden string: **111**

## How it works

The algorithm begins by placing the input qubits into an equal superposition of every possible binary string while the auxiliary qubit is prepared in the state \((|0⟩-|1⟩)/√2\). The oracle then encodes the hidden binary string into the phase of the quantum state using controlled-NOT gates. A second layer of Hadamard gates converts this phase information into measurable amplitudes through quantum interference. Measuring the input register directly reveals the hidden binary string with a single oracle query.

While a classical algorithm requires one oracle query for each bit of the hidden string, the Bernstein-Vazirani algorithm determines the entire string in just **one** query, demonstrating one of the earliest examples of quantum computational advantage.