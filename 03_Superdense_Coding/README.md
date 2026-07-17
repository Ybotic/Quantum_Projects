# Superdense Coding with Qiskit

Implementation of the Superdense Coding protocol — transmitting two classical bits by sending only one qubit using a shared entangled Bell pair.

## What's here

- `superdense_coding.py` — full Superdense Coding protocol: creates a Bell pair, encodes a two-bit message using quantum gates, decodes it, and recovers the original message through measurement

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python superdense_coding.py
```

## Results

**Superdense Coding protocol**

Message sent:

```
10
```

Circuit (Bell pair → encode message → decode → measure):

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

```
{'01': 1000}
```

The measurement corresponds to the original message after accounting for Qiskit's classical bit ordering (`c1 c0`), confirming successful transmission.

## How it works

Ybot and Snow first share an entangled Bell pair. To send one of four possible two-bit messages (`00`, `01`, `10`, or `11`), Ybot applies a specific quantum gate to his qubit before sending it to Snow. Snow then performs a decoding operation and measures both qubits, recovering the original two-bit message. Although only one qubit is transmitted, the shared entanglement allows two classical bits of information to be communicated.