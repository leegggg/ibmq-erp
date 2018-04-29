# Import the QISKit SDK
import qiskit

# Create a Quantum Register called "qr" with 2 qubits
qr = qiskit.QuantumRegister("qr", 2)
# Create a Classical Register called "cr" with 2 bits
cr = qiskit.ClassicalRegister("cr", 2)
# Create a Quantum Circuit called involving "qr" and "cr"
qc = qiskit.QuantumCircuit(qr, cr)

# Add a H gate on the 0th qubit in "qr", putting this qubit in superposition.
qc.h(qr[0])
# Add a CX (CNOT) gate on control qubit 0 and target qubit 1, putting
# the qubits in a Bell state.
qc.cx(qr[0], qr[1])
# Add a Measure gate to see the state.
# (Omitting the index applies an operation on all qubits of the register(s))
qc.measure(qr, cr)

# Create a Quantum Program for execution
qp = qiskit.QuantumProgram()
# Add the circuit you created to it, and call it the "bell" circuit.
# (You can add multiple circuits to the same program, for batch execution)
qp.add_circuit("bell", qc)

# See a list of available local simulators
print("Local backends: ", qiskit.backends.discover_local_backends())

# Compile and run the Quantum Program on a simulator backend
sim_result = qp.execute(
    "bell", backend='local_qasm_simulator', shots=20480, seed=None)

# Show the results
print("simulation: ", sim_result)
print(sim_result.get_counts("bell"))
