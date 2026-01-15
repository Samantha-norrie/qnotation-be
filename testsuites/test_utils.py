import httpx
from abc import ABC, abstractmethod
from errors.errors import (
    MESSAGE_HIGHER_INDEXED_CONTROL_QUBIT_ERROR,
    MESSAGE_UNKNOWN_ERROR,
)

EMPTY = ""

QISKIT = "qiskit"
PENNYLANE = "pennylane"
CIRQ = "cirq"

# QISKIT INPUTS
QISKIT_NO_GATES = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\n"
QISKIT_TYPO = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqv.h(0)"
QISKIT_SINGLE_QUBIT_SINGLE_HADAMARD = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.h(0)"
QISKIT_TOO_MANY_QUBITS = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(100)\n\n# Insert code below\nqc.h(0)"
QISKIT_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.cx(0, 1)\n"
QISKIT_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE_REVERSE = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.cx(1, 0)\n"
QISKIT_HIGHER_CONTROL_QUBIT_INDEX = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(3)\n\n# Insert code below\nqc.h(0)\nqc.cx(1, 0)\n"
QISKIT_NON_NEIGHBOURING_QUBITS = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(3)\n\n# Insert code below\nqc.h(0)\nqc.cx(0, 2)\n"
QISKIT_CCX = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(3)\n\n# Insert code below\nqc.x(0)\nqc.x(1)\nqc.ccx(0, 1, 2)\n"
QISKIT_CCZ = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(3)\n\n# Insert code below\nqc.x(0)\nqc.x(1)\nqc.ccz(0, 1, 2)\n"
QISKIT_CH = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.ch(0, 1)\n"
QISKIT_CPHASEA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cp(np.pi/4, 0, 1)\n"
QISKIT_CPHASEB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cp(np.pi/2, 0, 1)\n"
QISKIT_CPHASEC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cp(np.pi, 0, 1)\n"
QISKIT_CRXA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crx(np.pi/4, 0, 1)\n"
QISKIT_CRXB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crx(np.pi/2, 0, 1)\n"
QISKIT_CRXC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crx(np.pi, 0, 1)\n"
QISKIT_CRYA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cry(np.pi/4, 0, 1)\n"
QISKIT_CRYB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cry(np.pi/2, 0, 1)\n"
QISKIT_CRYC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cry(np.pi, 0, 1)\n"
QISKIT_CRZA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crz(np.pi/4, 0, 1)\n"
QISKIT_CRZB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crz(np.pi/2, 0, 1)\n"
QISKIT_CRZC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.crz(np.pi, 0, 1)\n"
QISKIT_CS = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cs(0, 1)\n"
QISKIT_CSDG = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.csdg(0, 1)\n"
QISKIT_CSWAP = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(3)\n\n# Insert code below\nqc.x(0)\nqc.x(1)\nqc.cswap(0, 1, 2)\n"
QISKIT_CSX = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.csx(0, 1)\n"
QISKIT_CX = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cx(0, 1)\n"
QISKIT_CY = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cy(0, 1)\n"
QISKIT_CZ = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.cz(0, 1)\n"
QISKIT_DCX = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.dcx(0, 1)\n"
QISKIT_ISWAP = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(2)\n\n# Insert code below\nqc.x(0)\nqc.iswap(0, 1)\n"
QISKIT_PHASEA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.p(np.pi/4, 0)\n"
QISKIT_PHASEB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.p(np.pi/2, 0)\n"
QISKIT_PHASEC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.p(np.pi, 0)\n"
QISKIT_R = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.r(np.pi/4, np.pi/2, 0)\n"
QISKIT_RV = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rv(np.pi/4, np.pi/2, np.pi, 0)\n"
QISKIT_RXA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rx(np.pi/4, 0)\n"
QISKIT_RXB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rx(np.pi/2, 0)\n"
QISKIT_RXC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rx(np.pi, 0)\n"
QISKIT_RYA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ry(np.pi/4, 0)\n"
QISKIT_RYB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ry(np.pi/2, 0)\n"
QISKIT_RYC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ry(np.pi, 0)\n"
QISKIT_RZA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rz(np.pi/4, 0)\n"
QISKIT_RZB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rz(np.pi/2, 0)\n"
QISKIT_RZC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rz(np.pi, 0)\n"
QISKIT_RXXA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rxx(np.pi/4, 0)\n"
QISKIT_RXXB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rxx(np.pi/2, 0)\n"
QISKIT_RXXC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rxx(np.pi, 0)\n"
QISKIT_RYYA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ryy(np.pi/4, 0)\n"
QISKIT_RYYB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ryy(np.pi/2, 0)\n"
QISKIT_RYYC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.ryy(np.pi, 0)\n"
QISKIT_RZZA = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rzz(np.pi/4, 0)\n"
QISKIT_RZZB = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rzz(np.pi/2, 0)\n"
QISKIT_RZZC = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.rzz(np.pi, 0)\n"
QISKIT_S = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.s(0)\n"
QISKIT_SDG = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.sdg(0)\n"
QISKIT_SWAP = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.swap(0, 1)\n"
QISKIT_T = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.t(0)\n"
QISKIT_TDG = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.tdg(0)\n"
QISKIT_U = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.u(np.pi/4, np.pi/2, np.pi, 0)\n"
QISKIT_Y = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.y(0)\n"
QISKIT_Z = "from qiskit import QuantumCircuit\nimport numpy as np\nqc = QuantumCircuit(1)\n\n# Insert code below\nqc.x(0)\nqc.y(0)\n"

# PENNYLANE INPUTS
PENNYLANE_EMPTY = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\n\treturn qml.state()\nqc()'
PENNYLANE_TYPO = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tql.Hadamard(wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_NON_NEIGHBOURING_QUBITS = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.Hadamard(wires=0)\n\tqml.CNOT(wires=[1, 0])\n\treturn qml.state()\nqc()'
PENNYLANE_HIGHER_CONTROL_QUBIT = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.Hadamard(wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_CCX = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=3)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.X(wires=1)\n\tqml.Toffoli(wires=[0, 1, 2])\n\treturn qml.state()\nqc()'
PENNYLANE_CH = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CH(wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASEA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhase(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASEB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhase(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASEC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhase(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT00A = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift00(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT00B = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift00(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT00C = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift00(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT01A = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift01(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT01B = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift01(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT01C = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift01(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT10A = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift10(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT10B = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift10(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CPHASESHIFT10C = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CPhaseShift10(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CROT = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRot(np.pi/4, np.pi/2, np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRXA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRX(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRXB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRX(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRXC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRX(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRYA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRY(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRYB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRY(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRYC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRY(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRZA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRZ(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRZB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRZ(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CRZC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CRZ(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CSWAP = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=3)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.X(wires=1)\n\tqml.CSWAP(wires=[0, 1, 2])\n\treturn qml.state()\nqc()'
PENNYLANE_CX = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CNOT(wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CY = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CY(wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_CZ = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.CZ(wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXXA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXX(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXXB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXX(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXXC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXX(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXYA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXY(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXYB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXY(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGXYC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingXY(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGYYA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingYY(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGYYB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingYY(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGYYC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingYY(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGZZA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingZZ(np.pi/4, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGZZB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingZZ(np.pi/2, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_ISINGZZC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.IsingZZ(np.pi, wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_R = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.Rot(np.pi/4, np.pi/2, np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RXA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RX(np.pi/4, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RXB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RX(np.pi/2, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RXC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RX(np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RYA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RY(np.pi/4, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RYB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RY(np.pi/2, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RYC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RY(np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RZA = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RZ(np.pi/4, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RZB = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RZ(np.pi/2, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_RZC = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.RZ(np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_S = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.S(wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_SWAP = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=2)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.SWAP(wires=[0, 1])\n\treturn qml.state()\nqc()'
PENNYLANE_U3 = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U3(wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_U1A = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U1(np.pi/4, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_U1B = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U1(np.pi/2, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_U1C = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U1(np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_U2A = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U2(np.pi/4, np.pi/2, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_U2B = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.U2(np.pi/2, np.pi, wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_Y = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.Y(wires=0)\n\treturn qml.state()\nqc()'
PENNYLANE_Z = 'import pennylane as qml\nimport numpy as np\ndev = qml.device("default.qubit", wires=1)\n@qml.qnode(dev)\ndef qc():\n\tqml.X(wires=0)\n\tqml.Z(wires=0)\n\treturn qml.state()\nqc()'

# CIRQ INPUTS
CIRQ_TYPO = "import cirq\nimport numpy as np\nqubit0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit()\ncircit.append([cirq.H(qubit0)])"
CIRQ_SINGLE_QUBIT_SINGLE_HADAMARD = "import cirq\nimport numpy as np\nqubit0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit()\ncircuit.append([cirq.H(qubit0)])"
CIRQ_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE = "import cirq\nimport numpy as np\nq0, q1 = cirq.LineQubit.range(2)\ncircuit = cirq.Circuit(cirq.CNOT(q0, q1))"
CIRQ_NON_NEIGHBOURING_QUBITS = "import cirq\nimport numpy as np\nq0, q1, q2 = cirq.LineQubit.range(3)\ncircuit = cirq.Circuit(cirq.H(q0),cirq.CNOT(q0, q2))"
CIRQ_CCX = "import cirq\nimport numpy as np\nq0, q1, q2 = cirq.LineQubit.range(3)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.X(q1),cirq.CCX(q0, q1, q2))"
CIRQ_CCZ = "import cirq\nimport numpy as np\nq0, q1, q2 = cirq.LineQubit.range(3)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.X(q1),cirq.CCZ(q0, q1, q2))"
CIRQ_CSWAP = "import cirq\nimport numpy as np\nq0, q1, q2 = cirq.LineQubit.range(3)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.X(q1),cirq.CSWAP(q0, q1, q2))"
CIRQ_ISWAP = "import cirq\nimport numpy as np\nq0, q1 = cirq.LineQubit.range(2)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.ISWAP(q0, q1))"
CIRQ_RXA = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rx(np.pi/4)(q0))"
CIRQ_RXB = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rx(np.pi/2)(q0))"
CIRQ_RXC = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rx(np.pi)(q0))"
CIRQ_RYA = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.ry(np.pi/4)(q0))"
CIRQ_RYB = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.ry(np.pi/2)(q0))"
CIRQ_RYC = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.ry(np.pi)(q0))"
CIRQ_RZA = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rz(np.pi/4)(q0))"
CIRQ_RZB = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rz(np.pi/2)(q0))"
CIRQ_RZC = "import cirq\nimport numpy as np\nq0 = cirq.LineQubit(0)\ncircuit = cirq.Circuit(cirq.X(q0),cirq.rz(np.pi)(q0))"

URL = "http://127.0.0.1:8000/notation_data"
HEADERS = {"Content-Type": "application/json"}
SUCCESS = 200
SERVER_ERR = 500
BAD_REQUEST_ERR = 400

MATRIX_GATE_LITTLE_ENDIAN = "matrix_gate_little_endian"
MATRIX_GATE_BIG_ENDIAN = "matrix_gate_big_endian"
MATRIX_GATE_TENSOR_LITTLE_ENDIAN = "matrix_gate_tensor_little_endian"
MATRIX_GATE_TENSOR_BIG_ENDIAN = "matrix_gate_tensor_big_endian"
MATRIX_STATE_LITTLE_ENDIAN = "matrix_state_little_endian"
MATRIX_STATE_BIG_ENDIAN = "matrix_state_big_endian"
CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN = "circuit_dirac_gate_little_endian"
CIRCUIT_DIRAC_GATE_BIG_ENDIAN = "circuit_dirac_gate_big_endian"
DIRAC_STATE_LITTLE_ENDIAN = "dirac_state_little_endian"
DIRAC_STATE_BIG_ENDIAN = "dirac_state_big_endian"
STATUS = "status"
NUM_QUBITS = "num_qubits"

# RESULTS

RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD = {
    "circuit_dirac_gate_big_endian": [
        {"content": [[0]], "key": 0, "type": "STATE"},
        {
            "content": [{"gate": "H", "gate_type": "GATE INFO"}],
            "key": 1,
            "type": "GATE",
        },
    ],
    "circuit_dirac_gate_little_endian": [
        {"content": [[0]], "key": 0, "type": "STATE"},
        {
            "content": [{"gate": "H", "gate_type": "GATE INFO"}],
            "key": 1,
            "type": "GATE",
        },
    ],
    "dirac_state_big_endian": [
        {"content": [{"bin": "0", "scalar": 1}], "key": 0, "type": "STATE"},
        {
            "content": [{"bin": "0", "scalar": 0.71}, {"bin": "1", "scalar": 0.71}],
            "key": 1,
            "type": "STATE",
        },
    ],
    "dirac_state_little_endian": [
        {"content": [{"bin": "0", "scalar": 1}], "key": 0, "type": "STATE"},
        {
            "content": [{"bin": "0", "scalar": 0.71}, {"bin": "1", "scalar": 0.71}],
            "key": 1,
            "type": "STATE",
        },
    ],
    "matrix_gate_big_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[0.71, 0.71], [0.71, -0.71]], "key": 1, "type": "GATE"},
    ],
    "matrix_gate_little_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[0.71, 0.71], [0.71, -0.71]], "key": 1, "type": "GATE"},
    ],
    "matrix_gate_tensor_big_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[[0.71, 0.71], [0.71, -0.71]]], "key": 1, "type": "GATE"},
    ],
    "matrix_gate_tensor_little_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[[0.71, 0.71], [0.71, -0.71]]], "key": 1, "type": "GATE"},
    ],
    "matrix_state_big_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[0.71], [0.71]], "key": 1, "type": "GATE"},
    ],
    "matrix_state_little_endian": [
        {"content": [[1], [0]], "key": 0, "type": "STATE"},
        {"content": [[0.71], [0.71]], "key": 1, "type": "GATE"},
    ],
    "message": "",
    "num_qubits": 1,
    "status": SUCCESS,
}
RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE = {
    "circuit_dirac_gate_big_endian": [
        {"content": [[0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                {"gate": "CX", "gate_type": "GATE INFO"},
                {"gate": "", "gate_type": "TARGET"},
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "circuit_dirac_gate_little_endian": [
        {"content": [[0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                {"gate": "", "gate_type": "TARGET"},
                {"gate": "CX", "gate_type": "GATE INFO"},
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "dirac_state_big_endian": [
        {"content": [{"bin": "00", "scalar": 1}], "type": "STATE", "key": 0},
        {"content": [{"bin": "00", "scalar": 1.0}], "type": "STATE", "key": 1},
    ],
    "dirac_state_little_endian": [
        {"content": [{"bin": "00", "scalar": 1}], "type": "STATE", "key": 0},
        {"content": [{"bin": "00", "scalar": 1.0}], "type": "STATE", "key": 1},
    ],
    "matrix_gate_big_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 0.0],
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "matrix_gate_little_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "matrix_gate_tensor_big_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                [
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                ]
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "matrix_gate_tensor_little_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {
            "content": [
                [
                    [1.0, 0.0, 0.0, 0.0],
                    [0.0, 0.0, 0.0, 1.0],
                    [0.0, 0.0, 1.0, 0.0],
                    [0.0, 1.0, 0.0, 0.0],
                ]
            ],
            "type": "GATE",
            "key": 1,
        },
    ],
    "matrix_state_big_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {"content": [[1.0], [0.0], [0.0], [0.0]], "type": "GATE", "key": 1},
    ],
    "matrix_state_little_endian": [
        {"content": [[1], [0], [0], [0]], "type": "STATE", "key": 0},
        {"content": [[1.0], [0.0], [0.0], [0.0]], "type": "GATE", "key": 1},
    ],
    "message": "",
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_HIGHER_CONTROL_QUBIT_INDEX = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_HIGHER_INDEXED_CONTROL_QUBIT_ERROR,
    "num_qubits": 0,
    "status": BAD_REQUEST_ERR,
}

RESULTS_NON_NEIGHBOURING_QUBITS = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTCCX = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CCX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': 'CCX', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '110', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '111', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '011', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '111', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 3,
    "status": SUCCESS,
}
RESULTS_TESTCCZ = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CCZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': 'CCZ', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '110', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '110', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '011', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '011', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 3,
    "status": SUCCESS,
}

RESULTS_TESTCH = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CH', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CH', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 0.71}, {'bin': '11', 'scalar': 0.71}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '11', 'scalar': 0.71}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.71, 0.71], [0.0, 0.0, 0.71, -0.71]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, 0.71], [0.0, 0.0, 1.0, 0.0], [0.0, 0.71, 0.0, -0.71]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.71, 0.71], [0.0, 0.0, 0.71, -0.71]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, 0.71], [0.0, 0.0, 1.0, 0.0], [0.0, 0.71, 0.0, -0.71]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [0.71], [0.71]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.71], [0.0], [0.71]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCPHASEA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CP', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCPHASEB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CP', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCPHASEC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CP', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCPHASESHIFT00A = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP00', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP00', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['1.41i', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['1.41i', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[['1.41i', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['1.41i', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT00B = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP00', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP00', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian":  [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[' i ', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[' i ', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[' i ', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[' i ', 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT00C = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP00', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP00', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[-1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[-1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT01A = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP01', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP01', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT01B = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP01', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP01', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT01C = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CP01', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CP01', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, -1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [-1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT10A = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT10B = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCPHASESHIFT10C = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCROT = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTCRXC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CRX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRX', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '11', 'scalar': '0.0-1.0i'}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-1.00i', 0.0, 0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-1.00i', 0.0, 0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian":  [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-1.00i', 0.0, 0.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-1.00i', 0.0, 0.0]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [0.0], ['0.0-1.0i']], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRXB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CRX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRX', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '11', 'scalar': '0.0-0.71i'}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, '-0.71i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.71i', 0.0, 0.71]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, '-0.71i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.71i', 0.0, 0.71]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, '-0.71i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.71i', 0.0, 0.71]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, '-0.71i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.71i', 0.0, 0.71]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.71], [0.0], ['0.0-0.71i']], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRXA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': 'CRX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'type': 'GATE', 'key': 2}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'type': 'STATE', 'key': 0}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 1}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRX', 'gate_type': 'GATE INFO'}], 'type': 'GATE', 'key': 2}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '10', 'scalar': 1.0}], 'type': 'STATE', 'key': 2}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'type': 'STATE', 'key': 0}, {'content': [{'bin': '01', 'scalar': 1.0}], 'type': 'STATE', 'key': 1}, {'content': [{'bin': '01', 'scalar': 0.92}, {'bin': '11', 'scalar': '0.0-0.38i'}], 'type': 'STATE', 'key': 2}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, '-0.38i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.38i', 0.0, 0.92]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'type': 'GATE', 'key': 1}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, '-0.38i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.38i', 0.0, 0.92]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_big_endian":  [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, '-0.38i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.38i', 0.0, 0.92]]], 'type': 'GATE', 'key': 2}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'type': 'GATE', 'key': 1}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, '-0.38i'], [0.0, 0.0, 1.0, 0.0], [0.0, '-0.38i', 0.0, 0.92]]], 'type': 'GATE', 'key': 2}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'type': 'GATE', 'key': 2}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'type': 'STATE', 'key': 0}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'type': 'GATE', 'key': 1}, {'content': [[0.0], [0.92], [0.0], ['0.0-0.38i']], 'type': 'GATE', 'key': 2}],
    "message": '',
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRYA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 0.92}, {'bin': '11', 'scalar': 0.38}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.92}, {'bin': '11', 'scalar': 0.38}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.92, -0.38], [0.0, 0.0, 0.38, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, -0.38], [0.0, 0.0, 1.0, 0.0], [0.0, 0.38, 0.0, 0.92]], 'key': 2, 'type': 'GATE'}] ,
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.92, -0.38], [0.0, 0.0, 0.38, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, 0.0, -0.38], [0.0, 0.0, 1.0, 0.0], [0.0, 0.38, 0.0, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.92], [0.38]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.92], [0.0], [0.38]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRYB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 0.71}, {'bin': '11', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '11', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.71, -0.71], [0.0, 0.0, 0.71, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, -0.71], [0.0, 0.0, 1.0, 0.0], [0.0, 0.71, 0.0, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.71, -0.71], [0.0, 0.0, 0.71, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, 0.0, -0.71], [0.0, 0.0, 1.0, 0.0], [0.0, 0.71, 0.0, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.71], [0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.71], [0.0], [0.71]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRYC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0], [0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0], [0.0, 0.0, 1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, -1.0], [0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCRZA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.92-0.38i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.92-0.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '0.54i', 0.0], [0.0, 0.0, 0.0, '1.31i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '0.54i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.31i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '0.54i', 0.0], [0.0, 0.0, 0.0, '1.31i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '0.54i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.31i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.92-0.38i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.92-0.38i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCRZB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.71-0.71i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.71-0.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '0.00i', 0.0], [0.0, 0.0, 0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '0.00i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '0.00i', 0.0], [0.0, 0.0, 0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '0.00i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.71-0.71i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.71-0.71i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCRZC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CRZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CRZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '-1.00i', 0.0], [0.0, 0.0, 0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '-1.00i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '-1.00i', 0.0], [0.0, 0.0, 0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '-1.00i', 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.0-1.0i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-1.0i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTCS = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CS', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CS', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']]], 'key': 2, 'type': 'GATE'}] ,
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCSDG= {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CSDG', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CSDG', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '-1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '-1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '-1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, '-1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCSWAP = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CSWAP', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': '', 'gate_type': 'CONTROL'}, {'gate': 'CSWAP', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '110', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '101', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '000', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '011', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '101', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0], [0], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [0.0], [1.0], [0.0], [0.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [0.0], [0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 3,
    "status": SUCCESS,
}

RESULTS_TESTCSX = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CSX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CSX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.50.5i'}, {'bin': '11', 'scalar': '0.5-0.5i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.50.5i'}, {'bin': '11', 'scalar': '0.5-0.5i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '1.00i', '0.00i'], [0.0, 0.0, '0.00i', '1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, '1.00i', 0.0, '0.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '0.00i', 0.0, '1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, '1.00i', '0.00i'], [0.0, 0.0, '0.00i', '1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, '1.00i', 0.0, '0.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, '0.00i', 0.0, '1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.50.5i'], ['0.5-0.5i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.50.5i'], [0.0], ['0.5-0.5i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCX = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0], [0.0, 1.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCY = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, ' i ', 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, ' i ', 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, ' i ', 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, 1.0, 0.0], [0.0, ' i ', 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTCZ = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'CZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'CZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, -1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTDCX = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'DCX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian":[{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'DCX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '11', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [0.0], [1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTISINGXXA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-0.38i'}, {'bin': '10', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.92}, {'bin': '10', 'scalar': '0.0-0.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian":  [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, 0.0, 0.0, '-0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['-0.38i', 0.0, 0.0, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, 0.0, 0.0, '-0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['-0.38i', 0.0, 0.0, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, 0.0, 0.0, '-0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['-0.38i', 0.0, 0.0, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, 0.0, 0.0, '-0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['-0.38i', 0.0, 0.0, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-0.38i'], [0.92], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.92], ['0.0-0.38i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}
RESULTS_TESTISINGXXB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-0.71i'}, {'bin': '10', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '10', 'scalar': '0.0-0.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, 0.0, 0.0, '-0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['-0.71i', 0.0, 0.0, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, 0.0, 0.0, '-0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['-0.71i', 0.0, 0.0, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, 0.0, 0.0, '-0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['-0.71i', 0.0, 0.0, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, 0.0, 0.0, '-0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['-0.71i', 0.0, 0.0, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-0.71i'], [0.71], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.71], ['0.0-0.71i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGXXC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], ['-1.00i', 0.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], ['-1.00i', 0.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], ['-1.00i', 0.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, 0.0, 0.0, '-1.00i'], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], ['-1.00i', 0.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-1.0i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.0-1.0i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTISINGXYA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.00.38i'}, {'bin': '10', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.92}, {'bin': '10', 'scalar': '0.00.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, '0.38i', 0.0], [0.0, '0.38i', 0.92, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, '0.38i', 0.0], [0.0, '0.38i', 0.92, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, '0.38i', 0.0], [0.0, '0.38i', 0.92, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.92, '0.38i', 0.0], [0.0, '0.38i', 0.92, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.00.38i'], [0.92], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.92], ['0.00.38i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGXYB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian":  [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.00.71i'}, {'bin': '10', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '10', 'scalar': '0.00.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, '0.71i', 0.0], [0.0, '0.71i', 0.71, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, '0.71i', 0.0], [0.0, '0.71i', 0.71, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, '0.71i', 0.0], [0.0, '0.71i', 0.71, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.71, '0.71i', 0.0], [0.0, '0.71i', 0.71, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.00.71i'], [0.71], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.71], ['0.00.71i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGXYC = {
    "circuit_dirac_gate_big_endian":  [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGXY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTISINGYYA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-0.38i'}, {'bin': '10', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.92}, {'bin': '10', 'scalar': '0.0-0.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, 0.0, 0.0, '0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['0.38i', 0.0, 0.0, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, 0.0, 0.0, '0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['0.38i', 0.0, 0.0, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, 0.0, 0.0, '0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['0.38i', 0.0, 0.0, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, 0.0, 0.0, '0.38i'], [0.0, 0.92, '-0.38i', 0.0], [0.0, '-0.38i', 0.92, 0.0], ['0.38i', 0.0, 0.0, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-0.38i'], [0.92], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.92], ['0.0-0.38i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGYYB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-0.71i'}, {'bin': '10', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 0.71}, {'bin': '10', 'scalar': '0.0-0.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, 0.0, 0.0, '0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['0.71i', 0.0, 0.0, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, 0.0, 0.0, '0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['0.71i', 0.0, 0.0, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, 0.0, 0.0, '0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['0.71i', 0.0, 0.0, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, 0.0, 0.0, '0.71i'], [0.0, 0.71, '-0.71i', 0.0], [0.0, '-0.71i', 0.71, 0.0], ['0.71i', 0.0, 0.0, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-0.71i'], [0.71], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.71], ['0.0-0.71i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGYYC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGYY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, 0.0, 0.0, ' i '], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], [' i ', 0.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, 0.0, 0.0, ' i '], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], [' i ', 0.0, 0.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, 0.0, 0.0, ' i '], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], [' i ', 0.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, 0.0, 0.0, ' i '], [0.0, 0.0, '-1.00i', 0.0], [0.0, '-1.00i', 0.0, 0.0], [' i ', 0.0, 0.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.0-1.0i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.0-1.0i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTISINGZZA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.920.38i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.920.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.54i', 0.0, 0.0, 0.0], [0.0, '1.31i', 0.0, 0.0], [0.0, 0.0, '1.31i', 0.0], [0.0, 0.0, 0.0, '0.54i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.54i', 0.0, 0.0, 0.0], [0.0, '1.31i', 0.0, 0.0], [0.0, 0.0, '1.31i', 0.0], [0.0, 0.0, 0.0, '0.54i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.54i', 0.0, 0.0, 0.0], [0.0, '1.31i', 0.0, 0.0], [0.0, 0.0, '1.31i', 0.0], [0.0, 0.0, 0.0, '0.54i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.54i', 0.0, 0.0, 0.0], [0.0, '1.31i', 0.0, 0.0], [0.0, 0.0, '1.31i', 0.0], [0.0, 0.0, 0.0, '0.54i']]], 'key': 2, 'type': 'GATE'}] ,
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.920.38i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.920.38i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGZZB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.00i', 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, '1.41i', 0.0], [0.0, 0.0, 0.0, '0.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.00i', 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, '1.41i', 0.0], [0.0, 0.0, 0.0, '0.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.00i', 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, '1.41i', 0.0], [0.0, 0.0, 0.0, '0.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.00i', 0.0, 0.0, 0.0], [0.0, '1.41i', 0.0, 0.0], [0.0, 0.0, '1.41i', 0.0], [0.0, 0.0, 0.0, '0.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['0.710.71i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
RESULTS_TESTISINGZZC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISINGZZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['-1.00i', 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, 0.0, 0.0, '-1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['-1.00i', 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, 0.0, 0.0, '-1.00i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[['-1.00i', 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, 0.0, 0.0, '-1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['-1.00i', 0.0, 0.0, 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, 0.0, 0.0, '-1.00i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTISWAP = {
    "circuit_dirac_gate_big_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}, {'gate': 'I', 'gate_type': 'NOT INVOLVED'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'ISWAP', 'gate_type': 'GATE INFO'}, {'gate': '', 'gate_type': 'TARGET'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'I', 'gate_type': 'NOT INVOLVED'}, {'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': '', 'gate_type': 'TARGET'}, {'gate': 'ISWAP', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '00', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '01', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '10', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]], [[1, 0], [0, 1]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[1, 0], [0, 1]], [[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, ' i ', 0.0], [0.0, ' i ', 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [0.0], [1.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i'], [0.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0], [0], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0], [0.0], [0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [0.0], ['i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTPHASEA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}] ,
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTPHASEB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTPHASEC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'P', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': -1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': -1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, -1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[1.0, 0.0], [0.0, -1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, -1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[1.0, 0.0], [0.0, -1.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [-1.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], [-1.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTR = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'R', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'R', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '-0.27-0.65i'}, {'bin': '1', 'scalar': '0.270.65i'}], 'key': 1, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '-0.27-0.65i'}, {'bin': '1', 'scalar': '0.270.65i'}], 'key': 1, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [['-0.92i', '0.38i'], ['0.92i', '0.38i']], 'key': 1, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [['-0.92i', '0.38i'], ['0.92i', '0.38i']], 'key': 1, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[['-0.92i', '0.38i'], ['0.92i', '0.38i']]], 'key': 1, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[['-0.92i', '0.38i'], ['0.92i', '0.38i']]], 'key': 1, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [['-0.27-0.65i'], ['0.270.65i']], 'key': 1, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [['-0.27-0.65i'], ['0.270.65i']], 'key': 1, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTR_QISKIT = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'R', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'R', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian":[{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.38}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.38}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, -0.38], [0.38, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, -0.38], [0.38, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, -0.38], [0.38, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, -0.38], [0.38, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.38], [0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.38], [0.92]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRC3X = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 3,
    "status": SUCCESS,
}

RESULTS_TESTRCCX = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 2,
    "status": SUCCESS,
}

RESULTS_TESTRV= {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRXA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-0.38i'}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-0.38i'}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, '-0.38i'], ['-0.38i', 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, '-0.38i'], ['-0.38i', 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, '-0.38i'], ['-0.38i', 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, '-0.38i'], ['-0.38i', 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-0.38i'], [0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-0.38i'], [0.92]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRXB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-0.71i'}, {'bin': '1', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-0.71i'}, {'bin': '1', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, '-0.71i'], ['-0.71i', 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, '-0.71i'], ['-0.71i', 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, '-0.71i'], ['-0.71i', 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, '-0.71i'], ['-0.71i', 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-0.71i'], [0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-0.71i'], [0.71]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRXC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RX', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': '0.0-1.0i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, '-1.00i'], ['-1.00i', 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, '-1.00i'], ['-1.00i', 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, '-1.00i'], ['-1.00i', 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, '-1.00i'], ['-1.00i', 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-1.0i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.0-1.0i'], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SERVER_ERR,
}

RESULTS_TESTRXXA = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRXXB = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRXXC = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.38}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.38}, {'bin': '1', 'scalar': 0.92}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, -0.38], [0.38, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.92, -0.38], [0.38, 0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, -0.38], [0.38, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.92, -0.38], [0.38, 0.92]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.38], [0.92]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.38], [0.92]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.71}, {'bin': '1', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -0.71}, {'bin': '1', 'scalar': 0.71}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, -0.71], [0.71, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.71, -0.71], [0.71, 0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, -0.71], [0.71, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.71, -0.71], [0.71, 0.71]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.71], [0.71]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-0.71], [0.71]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RY', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -1.0}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '0', 'scalar': -1.0}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, -1.0], [1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0, -1.0], [1.0, 0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, -1.0], [1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[[0.0, -1.0], [1.0, 0.0]]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[-1.0], [0.0]], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYYA = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYYB = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRYYC = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRZA = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}] ,
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.920.38i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.920.38i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.54i', 0.0], [0.0, '1.31i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.54i', 0.0], [0.0, '1.31i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.54i', 0.0], [0.0, '1.31i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.54i', 0.0], [0.0, '1.31i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.920.38i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.920.38i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRZB = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': '0.710.71i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.00i', 0.0], [0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['0.00i', 0.0], [0.0, '1.41i']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.00i', 0.0], [0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['0.00i', 0.0], [0.0, '1.41i']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['0.710.71i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRZC = {
    "circuit_dirac_gate_big_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "circuit_dirac_gate_little_endian": [{'content': [[0]], 'key': 0, 'type': 'STATE'}, {'content': [{'gate': 'X', 'gate_type': 'GATE INFO'}], 'key': 1, 'type': 'GATE'}, {'content': [{'gate': 'RZ', 'gate_type': 'GATE INFO'}], 'key': 2, 'type': 'GATE'}],
    "dirac_state_big_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "dirac_state_little_endian": [{'content': [{'bin': '0', 'scalar': 1}], 'key': 0, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 1.0}], 'key': 1, 'type': 'STATE'}, {'content': [{'bin': '1', 'scalar': 'i'}], 'key': 2, 'type': 'STATE'}],
    "matrix_gate_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['-1.00i', 0.0], [0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0, 1.0], [1.0, 0.0]], 'key': 1, 'type': 'GATE'}, {'content': [['-1.00i', 0.0], [0.0, ' i ']], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['-1.00i', 0.0], [0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_gate_tensor_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[[0.0, 1.0], [1.0, 0.0]]], 'key': 1, 'type': 'GATE'}, {'content': [[['-1.00i', 0.0], [0.0, ' i ']]], 'key': 2, 'type': 'GATE'}],
    "matrix_state_big_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "matrix_state_little_endian": [{'content': [[1], [0]], 'key': 0, 'type': 'STATE'}, {'content': [[0.0], [1.0]], 'key': 1, 'type': 'GATE'}, {'content': [[0.0], ['i']], 'key': 2, 'type': 'GATE'}],
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRZXA = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 1,
    "status": SUCCESS,
}

RESULTS_TESTRZXB = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTRZXC = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTRZZA = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTRZZB = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTRZZC = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTS = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTSDG = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTSWAP = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTT = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTTDG = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTUA = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU3= {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU1A = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU1B = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU1C = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU2A = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTU2B = {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTY= {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}

RESULTS_TESTZ= {
    "circuit_dirac_gate_big_endian": None,
    "circuit_dirac_gate_little_endian": None,
    "dirac_state_big_endian": None,
    "dirac_state_little_endian": None,
    "matrix_gate_big_endian": None,
    "matrix_gate_little_endian": None,
    "matrix_gate_tensor_big_endian": None,
    "matrix_gate_tensor_little_endian": None,
    "matrix_state_big_endian": None,
    "matrix_state_little_endian": None,
    "message": MESSAGE_UNKNOWN_ERROR,
    "num_qubits": 0,
    "status": SERVER_ERR,
}
async def send_request(qc_string, qc_type):
    payload = {"qc_string": qc_string, "qc_type": qc_type}
    async with httpx.AsyncClient() as client:
        response = await client.post(URL, json=payload, headers=HEADERS)
        return response.json()


class TestQNotation(ABC):
    """Abstract base class for test cases"""
    @classmethod
    @abstractmethod
    def setup_class(cls):
        pass

    @abstractmethod
    def test_status_code(self):
        pass

    @abstractmethod
    def test_num_qubits(self):
        pass

    @abstractmethod
    def test_circuit_dirac_little_endian(self):
        pass

    @abstractmethod
    def test_circuit_dirac_big_endian(self):
        pass

    @abstractmethod
    def test_dirac_state_little_endian(self):
        pass

    @abstractmethod
    def test_dirac_state_big_endian(self):
        pass

    @abstractmethod
    def test_matrix_gate_little_endian(self):
        pass

    @abstractmethod
    def test_matrix_gate_big_endian(self):
        pass

    @abstractmethod
    def test_matrix_gate_tensor_little_endian(self):
        pass

    @abstractmethod
    def test_matrix_gate_tensor_big_endian(self):
        pass

    @abstractmethod
    def test_matrix_state_little_endian(self):
        pass

    @abstractmethod
    def test_matrix_state_big_endian(self):
        pass


class TestQiskit(TestQNotation):
    qc_type = QISKIT


class TestPennylane(TestQNotation):
    qc_type = PENNYLANE


class TestCirq(TestQNotation):
    qc_type = CIRQ
