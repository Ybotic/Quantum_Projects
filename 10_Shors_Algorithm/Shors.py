from qiskit import QuantumCircuit, transpile
from qiskit.circuit.library import QFTGate
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def c_amod15(a, power):

    if a not in [2, 4, 7, 8, 11, 13]:
        raise ValueError("'a' must be one of 2, 4, 7, 8, 11, or 13")

    U = QuantumCircuit(4)

    for _ in range(power):

        if a == 2:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)

        elif a == 4:
            U.swap(1, 3)
            U.swap(0, 2)

        elif a == 8:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)

        elif a == 7:
            U.swap(0, 1)
            U.swap(1, 2)
            U.swap(2, 3)
            for q in range(4):
                U.x(q)

        elif a == 11:
            U.swap(1, 3)
            U.swap(0, 2)
            for q in range(4):
                U.x(q)

        elif a == 13:
            U.swap(2, 3)
            U.swap(1, 2)
            U.swap(0, 1)
            for q in range(4):
                U.x(q)

    U = U.to_gate()
    U.name = f"{a}^{power} mod 15"

    return U.control()

a = 2
n_count = 4

qc = QuantumCircuit(8, n_count)

qc.x(4)

for q in range(n_count):
    qc.h(q)

for q in range(n_count):
    qc.append(
        c_amod15(a, 2 ** q),
        [q] + [4, 5, 6, 7]
    )

qc.append(
    QFTGate(n_count).inverse(),
    range(n_count)
)

qc.measure(range(n_count), range(n_count))

simulator = AerSimulator()

compiled = transpile(qc, simulator)

result = simulator.run(compiled, shots=1024).result()

counts = result.get_counts()

print(counts)

plot_histogram(counts)
plt.show()