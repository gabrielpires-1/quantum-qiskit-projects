from qiskit.quantum_info import Statevector
from qiskit.circuit.library import HGate

# Criação de 1 qubit com estado 0
q = Statevector([1, 0])

# Aplica a porta Hadamard no qubit q
q = q.evolve(HGate())

# Realiza a medição do qubit após a aplicação da porta Hadamard
# 50% de chance do qubit estar no estado 1 e 50% de chance do qubit estar no estado 0
print(q.measure())

