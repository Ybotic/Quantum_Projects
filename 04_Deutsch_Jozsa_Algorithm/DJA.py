from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_deutsch_circuit(function_type):
    """
    function_type:
        "constant_0"
        "constant_1"
        "balanced_identity"
        "balanced_not"
    """

    qc = QuantumCircuit(2, 1)

    qc.x(1)

    qc.h(0)
    qc.h(1)

    qc.barrier()

    if function_type == "constant_0":
        pass

    elif function_type == "constant_1":
        qc.x(1)

    elif function_type == "balanced_identity":
        qc.cx(0, 1)

    elif function_type == "balanced_not":
        qc.cx(0, 1)
        qc.x(1)

    else:
        raise ValueError("Invalid function.")

    qc.barrier()

    qc.h(0)

    qc.barrier()

    qc.measure(0, 0)

    return qc

function = "constant_1"

qc = build_deutsch_circuit(function)

print("Oracle:", function)
print()

print(qc.draw(output="text"))

sim = AerSimulator()

result = sim.run(qc, shots=1000).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

if "0" in counts:
    print("\nThe function is CONSTANT.")

if "1" in counts:
    print("\nThe function is BALANCED.")