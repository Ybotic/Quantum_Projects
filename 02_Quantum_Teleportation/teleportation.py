from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector, random_statevector, partial_trace, DensityMatrix
import numpy as np

def build_teleportation_circuit(mystery_state):
    qc = QuantumCircuit(3, 3)

    qc.initialize(mystery_state, 0)
    qc.barrier()

    qc.h(1)
    qc.cx(1, 2)
    qc.barrier()

    qc.cx(0, 1)
    qc.h(0)
    qc.barrier()

    qc.measure(0, 0)
    qc.measure(1, 1)
    qc.barrier()

    with qc.if_test((qc.clbits[1], 1)):
        qc.x(2)
    with qc.if_test((qc.clbits[0], 1)):
        qc.z(2)

    return qc

mystery_state = random_statevector(2)
print("Original mystery state:", mystery_state)

qc = build_teleportation_circuit(mystery_state.data)
print(qc.draw(output='text'))

sim = AerSimulator(method='statevector')
qc_check = qc.copy()
qc_check.save_statevector()

result = sim.run(qc_check).result()
final_state = result.get_statevector()

ybot_density_matrix = partial_trace(DensityMatrix(final_state), [0, 1])
original_density_matrix = DensityMatrix(mystery_state)

fidelity = np.real(np.trace(ybot_density_matrix.data @ original_density_matrix.data))
print(f"Fidelity: {fidelity:.4f}")