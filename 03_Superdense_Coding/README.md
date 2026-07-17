# Superdense Coding with Qiskit

Implementation of the Superdense Coding protocol — transmitting two classical bits by sending only one qubit using a shared entangled Bell pair.

## What's here

- `superdense_coding.py` — full Superdense Coding protocol: creates a Bell pair, lets the user choose one of four two-bit messages, encodes it using quantum gates, decodes it, and recovers the original message through measurement.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python superdense_coding.py
```

The program will prompt you to choose one of the four possible messages:

```text
Choose a 2-bit message to send:
1. 00
2. 01
3. 10
4. 11
```

## Results

### Message `00`

Circuit:

```
     ┌───┐      ░       ░      ┌───┐ ░ ┌─┐
q_0: ┤ H ├──■───░───────░───■──┤ H ├─░─┤M├───
     └───┘┌─┴─┐ ░       ░ ┌─┴─┐└───┘ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░───────░─┤ X ├──────░──╫─┤M├
          └───┘ ░       ░ └───┘      ░  ║ └╥┘
c: 2/═══════════════════════════════════╩══╩═
                                        0  1
```

Measurement Results:

```text
{'00': 1000}
```

Recovered message: **00**

---

### Message `01`

Circuit:

```
     ┌───┐      ░ ┌───┐ ░      ┌───┐ ░ ┌─┐
q_0: ┤ H ├──■───░─┤ X ├─░───■──┤ H ├─░─┤M├───
     └───┘┌─┴─┐ ░ └───┘ ░ ┌─┴─┐└───┘ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░───────░─┤ X ├──────░──╫─┤M├
          └───┘ ░       ░ └───┘      ░  ║ └╥┘
c: 2/═══════════════════════════════════╩══╩═
                                        0  1
```

Measurement Results:

```text
{'01': 1000}
```

Recovered message: **01**

---

### Message `10`

Circuit:

```
     ┌───┐      ░ ┌───┐ ░      ┌───┐ ░ ┌─┐
q_0: ┤ H ├──■───░─┤ Z ├─░───■──┤ H ├─░─┤M├───
     └───┘┌─┴─┐ ░ └───┘ ░ ┌─┴─┐└───┘ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░───────░─┤ X ├──────░──╫─┤M├
          └───┘ ░       ░ └───┘      ░  ║ └╥┘
c: 2/═══════════════════════════════════╩══╩═
                                        0  1
```

Measurement Results:

```text
{'10': 1000}
```

Recovered message: **10**

---

### Message `11`

Circuit:

```
     ┌───┐      ░ ┌───┐┌───┐ ░      ┌───┐ ░ ┌─┐
q_0: ┤ H ├──■───░─┤ X ├┤ Z ├─░───■──┤ H ├─░─┤M├───
     └───┘┌─┴─┐ ░ └───┘└───┘ ░ ┌─┴─┐└───┘ ░ └╥┘┌─┐
q_1: ─────┤ X ├─░────────────░─┤ X ├──────░──╫─┤M├
          └───┘ ░            ░ └───┘      ░  ║ └╥┘
c: 2/════════════════════════════════════════╩══╩═
                                             0  1
```

Measurement Results:

```text
{'11': 1000}
```

Recovered message: **11**

## How it works

Ybot and Snow first share an entangled Bell pair. To communicate, Ybot chooses one of four possible two-bit messages (`00`, `01`, `10`, or `11`) and applies a corresponding quantum operation to his qubit:

| Message | Gate Applied |
|---------|--------------|
| `00` | None |
| `01` | X |
| `10` | Z |
| `11` | X then Z |

Ybot then sends **only his single qubit** to Snow. Using the shared entanglement, Snow applies a CNOT gate followed by a Hadamard gate to decode the message and measures both qubits.

Although only **one qubit** is transmitted, the protocol successfully communicates **two classical bits** of information, demonstrating how entanglement can increase the information-carrying capacity of quantum communication.