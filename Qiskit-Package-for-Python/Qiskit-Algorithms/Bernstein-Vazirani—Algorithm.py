from qiskit import *
from qiskit.tools.visualization plot_histogram

#to generalise for any given secretnumber
secretnumber = '#number'

#
circuit = QuantumCircuit(len(secretnumber)+1,len(secretnumber))
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))
circuit.barrier()
circuit.draw(output = 'mpl')

#
for ii, yesno in enumerate(reversed(secretnumber)):
  if yesno == '1':
    circuit.cx(ii, len(secretnumber))

circuit.barrier() #all barrier insertions are for visual purposes for the .draw function only, and are not a part of the algorithm
circuit.draw(output = 'mpl')

#
circuit.h(range(len(secretnumber)))
circuit.barrier()
circuit.draw(output = 'mpl')

#
circuit.measure(range(len(secretnumber)), range(len(secretnumber)))
circuit.draw(output = 'mpl')

#
simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts)

#to compare calculated number with secretnumber
print(secretnumber)

