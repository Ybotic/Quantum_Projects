# Quantum Teleportation with Qiskit

Implementation of the quantum teleportation protocol — transferring an unknown qubit's quantum state from one qubit to another using entanglement and classical communication, verified via state fidelity.

## What's here

- `teleportation.py` — full 3-qubit teleportation protocol: prepares a random unknown state, teleports it, and verifies success by computing fidelity between the original and teleported state

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python teleportation.py
```

## Results

**Teleportation protocol**

Original mystery state on Ybot's qubit :

Statevector([0.68976666-0.58094645j, 0.32651485-0.28303926j], dims=(2,))

Circuit (entangle → measure → classically-conditioned correction on Snow's qubit ):

Original mystery state: Statevector([0.68976666-0.58094645j, 0.32651485-0.28303926j]

```
            dims=(2,))
     ┌───────────────────────────────────────────────┐ ░            ░      ┌───┐ ░ ┌─┐    ░                                                     
q_0: ┤ Initialize(0.68977-0.58095j,0.32651-0.28304j) ├─░────────────░───■──┤ H ├─░─┤M├────░─────────────────────────────────────────────────────
     └───────────────────────────────────────────────┘ ░ ┌───┐      ░ ┌─┴─┐└───┘ ░ └╥┘┌─┐ ░                                                     
q_1: ──────────────────────────────────────────────────░─┤ H ├──■───░─┤ X ├──────░──╫─┤M├─░─────────────────────────────────────────────────────
                                                       ░ └───┘┌─┴─┐ ░ └───┘      ░  ║ └╥┘ ░   ┌──────  ┌───┐ ───────┐   ┌──────  ┌───┐ ───────┐ 
q_2: ──────────────────────────────────────────────────░──────┤ X ├─░────────────░──╫──╫──░───┤ If-0  ─┤ X ├  End-0 ├───┤ If-0  ─┤ Z ├  End-0 ├─
                                                       ░      └───┘ ░            ░  ║  ║  ░   └──╥───  └───┘ ───────┘   └──╥───  └───┘ ───────┘ 
                                                                                    ║  ║    ┌────╨────┐               ┌────╨────┐               
c: 3/═══════════════════════════════════════════════════════════════════════════════╩══╩════╡ c_1=0x1 ╞═══════════════╡ c_0=0x1 ╞═══════════════
                                                                                    0  1    └─────────┘               └─────────┘               
```
**Fidelity: 1.0000** — a perfect result, confirming Snow's qubit ended up in exactly the same state Ybot started with, with no information loss.

## How it works

Ybot holds an unknown qubit state she wants to send to Snow. He can't copy it directly (no-cloning theorem), so instead he and Snow pre-share an entangled pair. Ybot entangles his mystery qubit with his half of the pair, measures both of his qubits, and sends the two classical bits to Snow. Snow applies a correction gate based on those bits, and his qubit ends up in Ybot's original state — without the qubit itself ever traveling.