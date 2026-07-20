from qiskit import QuantumCircuit
from math import pi

qc = QuantumCircuit(3)


qc.x(0)

#most significant
qc.h(2)

#if q1 is 1 then rotate 2 by pi/2
qc.cp(pi/2, 1, 2)

#if q0 is 1 then rotate 2 by pi/4
qc.cp(pi/4, 0, 2)

qc.h(1)

qc.cp(pi/2, 0, 1)

qc.h(0)
qc.swap(0,2)

print(qc.draw())