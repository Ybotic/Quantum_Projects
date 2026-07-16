# Bell State with Qiskit

A simple Qiskit implementation that creates a Bell state: the simplest example of quantum entanglement. The circuit places one qubit into superposition using a Hadamard gate and then entangles it with a second qubit using a CNOT gate.

By measuring both qubits repeatedly, the simulation demonstrates the characteristic correlated outcomes of an entangled quantum system.

## What's here

- `bell_state.py` — creates an entangled Bell pair and shows the correlated measurement outcomes that make teleportation possible

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python bell_state.py
```

## Results

**Step 1 — Bell pair entanglement**

```
     ┌───┐     ┌─┐   
q_0: ┤ H ├──■──┤M├───
     └───┘┌─┴─┐└╥┘┌─┐
q_1: ─────┤ X ├─╫─┤M├
          └───┘ ║ └╥┘
c: 2/═══════════╩══╩═
                0  1 
```
{'00': 515, '11': 485}

Only `00` and `11` show up across 1000 runs — confirming the two qubits are entangled (perfectly correlated outcomes, each individually random).

