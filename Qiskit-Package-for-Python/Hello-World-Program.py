#import the necessary items into the environment 
from qiskit import *
from qiskit.tools.monitor import *
from qiskit.tools.visualization import *
IBMQ.save_account('#IBM Quantum Experience API Key')

#set up and visualise the quantum circuit
circuit = QuantumCircuit(2,2)
%matplotlib inline
circuit.draw(initial_state = True)

#apply the Hadamard gate to the first qubit 
circuit.h(0)
circuit.draw()

#create entanglement between qubits if index 0 and 1 and measure
circuit.cx(0,1)
circuit.measure([0,1],[0,1])

#run the code in a real quantum computer through IBM
IBMQ.load_account()
provider = IBMQ.get_provider('ibm-q')
provider.backends()
qcomp = provider.get_backend('#name of backend')
job = execute(circuit, backend = qcomp)
job_monitor(job)

#visualise the results
#They should be approximately 50:50 between 00 and 11, with a few errors given by the hardware where the entanglement has failed
result = job.result()
count = result.get_counts(circuit)
plot_histogram(count)
