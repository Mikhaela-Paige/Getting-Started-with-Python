from qiskit import *
from qiskit.tools.visualization import *
from qiskit.visualization import *

circuit = QuantumCircuit(2,2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure([0,1],[0,1])
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, simulator).result()
plot_histogram(result.get_counts(circuit))

backend = Aer.get_backend('statevector_simulator')
result = execute(circuit, backend).result()
final_state = result.get_statevector()
plot_bloch_multivector(final_state)
