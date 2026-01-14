# QNotation

[QNotation](https://qnotation.vercel.app/) is a web application designed to help users convert between circuit, Dirac, and matrix notation in the context of quantum computing.
## Workflow
QNotation is available at [https://qnotation.vercel.app/](https://qnotation.vercel.app/), so no setup is required! This section walks you through running your quantum circuits in the app.

### 1. Inputting your quantum circuit into QNotation
QNotation takes in [Qiskit](https://www.ibm.com/quantum/qiskit), [PennyLane](https://pennylane.ai/), [Cirq](https://quantumai.google/cirq) quantum circuits. which are inputted through the code editor on the right side of the app.
Here are some points to keep in mind while creating your quantum circuits for QNotation:
- Code must be added below ```Insert code below``` comments.
- quantum circuits with 1 to 5 qubits can be run in the app.
- measurement and classical operations are currently not supported.
- Neighbouring qubits must be used for multi-qubit gates.
  - ✅ ```qc.cx(0, 1)```
  - ❌ ```qc.cx(0, 2)```
- Control qubit(s) must have a lower qubit index than their respective target(s)
  - ✅ ```qc.cx(0, 1)```
  - ❌ ```qc.cx(1, 0)```
- Most gates are supported by the app. A list of supported gates can be found below

Example input can be found in the *EXAMPLES* dropdown.

### 2. Interpreting notation data
QNotation contains interactive visualizations for circuit, Dirac, and matrix. Clicking on different sections of a notation will reveal its equivalent sections in the other notations (in orange). The quantum state after the selected sections is shown on the right of the Dirac and matrix visualization subsections.

#### 2.1 Additional features for exploring
A couple of toggles have been included on the bottom right of the app:
- **Little endian (LE) toggle**: allows for toggling between little endian and big endian ordering
- **Tensor (⊗) toggle**: allows matrix notation visualization to be broken down into tensor products (for quantum circuits with 3 qubits or less)

## Publications
- Samantha Norrie, Anthony Estey, Hausi Müller, Ulrike Stege, [QNotation: A Visual Browser-Based Notation Translator for Learning Quantum Computing](https://ieeexplore.ieee.org/document/10821137), technical paper published in the proceedings of QSEEC 2024 (QCE 2024)
- Samantha Norrie, Anthony Estey, [QNotation: An Interactive Visual Tool to Lower Learning Barriers in Quantum Computing](https://ieeexplore.ieee.org/document/10313602), extended abstract and poster published in QCE 2023 –*Jupyter notebook version*

## Disclaimer
QNotation is currently in **beta**. Although it has been tested, it may still contain bugs or unexpected behaviour.

### Qiskit Gates Supported by QNotation
- [CCX: Controlled-controlled-x (Toffoli) gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CCXGate)
- [CCZ: Controlled-controlled-z gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CCZGate)
- [CH: Controlled-hadamard gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CHGate)
- [CP: Controlled-phase gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CPhaseGate)
- [CRX: Controlled-rx gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CRXGate)
- [CRY: Controlled-ry gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CRXGate)
- [CRZ: Controlled-rz gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CRZGate)
- [CSDG: Controlled-s^dagger gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CSdgGate)
- [CS: Controlled-s gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CSGate)
- [CSWAP: Controlled-swap gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CSWAPGate)
- [CU: Controlled-u gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CUGate)
- [CX: Controlled-x gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CXGate)
- [CY: Controlled-y gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CYGate)
- [CZ: Controlled-z gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.CZGate)
- [DCX: Double-Controlled-x gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.DCXGate)
- [H: Hadamard gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.HGate)
- [ID: Identity gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.IGate)
- [ISWAP: I-swap gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.ISWAPGate)
- [RCCX: Margolous gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RCCXGate)
- [R: Rot gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RGate)
- [RV: Rot-v gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RVGate)
- [RX: Rot-x gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RXGate)
- [RXX: Rot-xx gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RXXGate)
- [RXY: Rot-xy gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RXYGate)
- [RY: Rot-y gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RYGate)
- [RYY: Rot-yy gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RYYGate)
- [RZ: Rot-z gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RZGate)
- [RZX: Rot-z gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RZXGate)
- [RZZ: Rot-zz gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.RZZGate)
- [SDG: S^dagger gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SDGGate)
- [S: S gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SGate)
- [SWAP: Swap gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SWAPGate)
- [SX: SX gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SXGate)
- [SXDG: SX^dagger gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.SXDGGate)
- [TDG: T^dagger gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.TDGGate)
- [T: T gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.TGate)
- [U: U gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.UGate)
- [X: Pauli-x gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.XGate)
- [Y: Pauli-y gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.YGate)
- [Z: Pauli-Z gate](https://docs.quantum.ibm.com/api/qiskit/qiskit.circuit.library.ZGate)

### PennyLane Gates Supported by QNotation
- [CH: Controlled-hadamard gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CH.html)
- [CNOT: Controlled-x gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CNOT.html)
- [CPhase: Controlled-phase gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CPhase.html)
- [CPhaseShift00: Controlled-phase-shift00 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CPhaseShift00.html)
- [CPhaseShift01: Controlled-phase-shift01 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CPhaseShift01.html)
- [CPhaseShift10: Controlled-phase-shift10 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CPhaseShift10.html)
- [CRot: Controlled-rot gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRot.html)
- [CRX: Controlled-rx gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRX.html)
- [CRY: Controlled-ry gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRY.html)
- [CRZ: Controlled-rz gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CRZ.html)
- [CSWAP: Controlled-swap gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CSWAP.html)
- [CY: Controlled-y gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CY.html)
- [CZ: Controlled-z gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.CZ.html)
- [ECR: Controlled-echoed-rot gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.ECR.html)
- [Hadamard: Hadamard gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.Hadamard.html)
- [I: Identity gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.I.html)
- [IsingXX: Ising-XX gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.IsingXX.html)
- [IsingXY: Ising-XY gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.IsingXY.html)
- [IsingYY: Ising-YY gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.IsingYY.html)
- [IsingZZ: Ising-XX gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.IsingZZ.html)
- [ISwap: I-Swap gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.ISwap.html)
- [PauliX: Pauli-X gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.PauliX.html)
- [PauliY: Pauli-Y gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.PauliY.html)
- [PauliZ: Pauli-Z gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.PauliZ.html)
- [PhaseShift: Phase-shift gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.PhaseShift.html)
- [PSwap: Phase-swap gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.PSwap.html)
- [Rot: Rot gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.Rot.html)
- [RX: Rot-x gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.RX.html)
- [RY: Rot-y gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.RY.html)
- [RZ: Rot-z gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.RZ.html)
- [S: S gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.S.html)
- [SISWAP: Sqrt-i-swap gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.SISWAP.html)
- [SWAP: Swap gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.SWAP.html)
- [SX: SX gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.SX.html)
- [T: T gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.T.html)
- [Toffoli: Toffoli (CCX) gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.Toffoli.html)
- [U1: U1 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.U1.html)
- [U2: U2 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.U2.html)
- [U3: U3 gate](https://docs.pennylane.ai/en/stable/code/api/pennylane.U3.html)

### Cirq Gates Supported by QNotation
- [CCX: Controlled-controlled-x gate](https://quantumai.google/cirq/build/gates)
- [CCZ: Controlled-controlled-z gate](https://quantumai.google/cirq/build/gates)
- [CNOT: Controlled-x gate](https://quantumai.google/cirq/build/gates)
- [CSWAP: Controlled-swap gate](https://quantumai.google/cirq/build/gates)
- [CZ: Controlled-z gate](https://quantumai.google/cirq/build/gates)
- [H: Hadamard gate](https://quantumai.google/cirq/build/gates)
- [ISWAP: I-Swap gate](https://quantumai.google/cirq/build/gates)
- [MatrixGate: Matrix gate](https://quantumai.google/cirq/build/gates)
- [rx: Rot-x gate](https://quantumai.google/cirq/build/gates)
- [ry: Rot-y gate](https://quantumai.google/cirq/build/gates)
- [rz: Rot-z gate](https://quantumai.google/cirq/build/gates)
- [S: S gate](https://quantumai.google/cirq/build/gates)
- [SWAP: Swap gate](https://quantumai.google/cirq/build/gates)
- [T: T gate](https://quantumai.google/cirq/build/gates)
- [X: Not gate](https://quantumai.google/cirq/build/gates)
- [XX: Not-not gate](https://quantumai.google/cirq/build/gates)
- [Y: Y gate](https://quantumai.google/cirq/build/gates)
- [YY: YY gate](https://quantumai.google/cirq/build/gates)
- [Z: Z gate](https://quantumai.google/cirq/build/gates)
- [ZZ: ZZ gate](https://quantumai.google/cirq/build/gates)