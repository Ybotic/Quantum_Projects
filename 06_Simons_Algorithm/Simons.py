from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.compiler import transpile
import numpy as np


# Choose the hidden string s

hidden_string = "101"
n = len(hidden_string)

oracle = QuantumCircuit(2 * n)

for i in range(n):
    oracle.cx(i, n + i)

# Implement the hidden string
pivot = hidden_string.find("1")

if pivot != -1:
    for i, bit in enumerate(hidden_string):
        if bit == "1":
            oracle.cx(pivot, n + i)


qc = QuantumCircuit(2 * n, n)

qc.h(range(n))

qc.compose(oracle, inplace=True)

qc.h(range(n))

qc.measure(range(n), range(n))

simulator = AerSimulator()

compiled = transpile(qc, simulator)

result = simulator.run(compiled, shots=1024).result()

counts = result.get_counts()

print("Hidden string:", hidden_string)
print("\nMeasurement Results:")
print(counts)

print("\nCircuit:")
print(qc.draw())