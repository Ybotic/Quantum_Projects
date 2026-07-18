from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

# Superposition
qc.h([0, 1])

# Oracle (marks |11>)
qc.cz(0, 1)

# Diffusion operator
qc.h([0, 1])
qc.z([0, 1])
qc.cz(0, 1)
qc.h([0, 1])

# Measure
qc.measure([0, 1], [0, 1])

# Simulate
simulator = AerSimulator()
compiled = transpile(qc, simulator)

result = simulator.run(compiled, shots=1000).result()

counts = result.get_counts()

print("Measurement Results:")
print(counts)

print("\nCircuit:")
print(qc.draw())