from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFT
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
from numpy import pi
import matplotlib.pyplot as plt

n_count = 3

qc = QuantumCircuit(n_count + 1, n_count)

qc.x(3)

for qubit in range(n_count):
    qc.h(qubit)

qc.cp(pi/4, 0, 3)
qc.cp(pi/2, 1, 3)
qc.cp(pi, 2, 3)

qc.append(
    QFT(num_qubits=n_count, inverse=True),
    range(n_count)
)

qc.measure(range(n_count), range(n_count))

simulator = AerSimulator()
compiled = transpile(qc, simulator)
job = simulator.run(compiled, shots=1024)

result = job.result()
counts = result.get_counts()

print(counts)

plot_histogram(counts)
plt.show()