from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_superdense_coding_circuit(message):
    qc = QuantumCircuit(2, 2)

    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()

    if message == "00":
        pass

    elif message == "01":
        qc.x(0)

    elif message == "10":
        qc.z(0)

    elif message == "11":
        qc.x(0)
        qc.z(0)

    else:
        raise ValueError("Message must be one of: 00, 01, 10, 11")

    qc.barrier()

    qc.cx(0, 1)
    qc.h(0)

    qc.barrier()

    qc.measure([0, 1], [0, 1])

    return qc


print("Choose a 2-bit message to send:")
print("1. 00")
print("2. 01")
print("3. 10")
print("4. 11")

options = {
    "1": "00",
    "2": "01",
    "3": "10",
    "4": "11"
}

while True:
    choice = input("\nEnter your choice (1-4): ").strip()

    if choice in options:
        message = options[choice]
        break

    print("Invalid choice. Please enter 1, 2, 3, or 4.")

qc = build_superdense_coding_circuit(message)

print(f"\nMessage sent: {message}\n")
print(qc.draw(output="text"))

sim = AerSimulator()

result = sim.run(qc, shots=1000).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)