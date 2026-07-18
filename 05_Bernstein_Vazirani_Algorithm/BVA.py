from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def build_bernstein_vazirani_circuit(secret):
    n = len(secret)

    qc = QuantumCircuit(n + 1, n)

    qc.x(n)

    for i in range(n + 1):
        qc.h(i)

    qc.barrier()

    for i, bit in enumerate(secret):
        if bit == "1":
            qc.cx(i, n)

    qc.barrier()

    for i in range(n):
        qc.h(i)

    qc.barrier()

    qc.measure(range(n), range(n))

    return qc


print("Choose the hidden string:")
print("1. 000")
print("2. 101")
print("3. 110")
print("4. 111")

options = {
    "1": "000",
    "2": "101",
    "3": "110",
    "4": "111"
}

while True:
    choice = input("\nEnter your choice (1-4): ").strip()

    if choice in options:
        secret = options[choice]
        break

    print("Invalid choice. Please enter 1, 2, 3, or 4.")

qc = build_bernstein_vazirani_circuit(secret)

print(f"\nHidden string: {secret}\n")
print(qc.draw(output="text"))

sim = AerSimulator()

result = sim.run(qc, shots=1000).result()

counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)