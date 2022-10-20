from qiskit import *
from qiskit.tools.visualization plot_histogram

#to generalise for any given secretnumber
secretnumber = '#number'

#circuit set-up
circuit = QuantumCircuit(len(secretnumber)+1,len(secretnumber)) #(The no. of bits in secretnumber + 1, the no. of bits in secretnumber)
circuit.h(range(len(secretnumber))) #[all of the bits in the secret number]
circuit.x(len(secretnumber))#[the + 1 bit]
circuit.h(len(secretnumber))#[the + 1 bit]
circuit.barrier()
circuit.draw(output = 'mpl')

#to find (bit that is equal to one, the + 1 bit)
for ii, yesno in enumerate(reversed(secretnumber)):
  if yesno == '1':
    circuit.cx(ii, len(secretnumber))

circuit.barrier() #all barrier insertions are for visual purposes for the .draw function only, and are not a part of the algorithm
circuit.draw(output = 'mpl')

circuit.h(range(len(secretnumber))) #[all of the bits in the secret number]
circuit.barrier()
circuit.draw(output = 'mpl')

circuit.measure(range(len(secretnumber)), range(len(secretnumber)))  #[all of the bits in the secret number], [classical bit for all of the bits in the secret number]
circuit.draw(output = 'mpl')

simulator = Aer.get_backend('qasm_simulator')
result = execute(circuit, backend = simulator, shots = 1).result()
counts = result.get_counts()
print(counts) #outputs the secretnumber

#to compare calculated number with secretnumber
print(secretnumber)

