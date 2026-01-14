import asyncio
from .test_utils import (
    TestQiskit,
    send_request,
    EMPTY,
    STATUS,
    BAD_REQUEST_ERR,
    NUM_QUBITS,
    CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN,
    CIRCUIT_DIRAC_GATE_BIG_ENDIAN,
    DIRAC_STATE_LITTLE_ENDIAN,
    DIRAC_STATE_BIG_ENDIAN,
    MATRIX_GATE_LITTLE_ENDIAN,
    MATRIX_GATE_BIG_ENDIAN,
    MATRIX_GATE_TENSOR_LITTLE_ENDIAN,
    MATRIX_GATE_TENSOR_BIG_ENDIAN,
    MATRIX_STATE_LITTLE_ENDIAN,
    MATRIX_STATE_BIG_ENDIAN,
    QISKIT_TYPO,
    QISKIT_SINGLE_QUBIT_SINGLE_HADAMARD,
    SUCCESS,
    RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD,
    QISKIT_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE,
    RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE,
    QISKIT_HIGHER_CONTROL_QUBIT_INDEX,
    RESULTS_HIGHER_CONTROL_QUBIT_INDEX,
    QISKIT_NON_NEIGHBOURING_QUBITS,
    RESULTS_NON_NEIGHBOURING_QUBITS,
    RESULTS_TESTCCX,
    QISKIT_CCX,
    RESULTS_TESTCCZ,
    QISKIT_CCZ,
    RESULTS_TESTCH,
    QISKIT_CH,
    RESULTS_TESTCPHASEA,
    QISKIT_CPHASEA,
    RESULTS_TESTCPHASEB,
    QISKIT_CPHASEB,
    RESULTS_TESTCPHASEC,
    QISKIT_CPHASEC,
    RESULTS_TESTCRXA,
    QISKIT_CRXA,
    RESULTS_TESTCRXB,
    QISKIT_CRXB,
    RESULTS_TESTCRXC,
    QISKIT_CRXC,
    RESULTS_TESTCRYA,
    QISKIT_CRYA,
    RESULTS_TESTCRYB,
    QISKIT_CRYB,
    RESULTS_TESTCRYC,
    QISKIT_CRYC,
    RESULTS_TESTCRZA,
    QISKIT_CRZA,
    RESULTS_TESTCRZB,
    QISKIT_CRZB,
    RESULTS_TESTCRZC,
    QISKIT_CRZC,
    RESULTS_TESTCS,
    QISKIT_CS,
    RESULTS_TESTCSDG,
    QISKIT_CSDG,
    RESULTS_TESTCSWAP,
    QISKIT_CSWAP,
    RESULTS_TESTCSX,
    QISKIT_CSX,
    RESULTS_TESTCX,
    QISKIT_CX,
    RESULTS_TESTCY,
    QISKIT_CY,
    RESULTS_TESTCZ,
    QISKIT_CZ,
    RESULTS_TESTDCX,
    QISKIT_DCX,
    RESULTS_TESTISWAP,
    QISKIT_ISWAP,
    RESULTS_TESTPHASEA,
    QISKIT_PHASEA,
    RESULTS_TESTPHASEB,
    QISKIT_PHASEB,
    RESULTS_TESTPHASEC,
    QISKIT_PHASEC,
    RESULTS_TESTR,
    QISKIT_R,
    RESULTS_TESTRV,
    QISKIT_RV,
    RESULTS_TESTRXA,
    QISKIT_RXA,
    RESULTS_TESTRXB,
    QISKIT_RXB,
    RESULTS_TESTRXC,
    QISKIT_RXC,
    RESULTS_TESTRYA,
    QISKIT_RYA,
    RESULTS_TESTRYB,
    QISKIT_RYB,
    RESULTS_TESTRYC,
    QISKIT_RYC,
    RESULTS_TESTRZA,
    QISKIT_RZA,
    RESULTS_TESTRZB,
    QISKIT_RZB,
    RESULTS_TESTRZC,
    QISKIT_RZC,
    RESULTS_TESTRXXA,
    QISKIT_RXXA,
    RESULTS_TESTRXXB,
    QISKIT_RXXB,
    RESULTS_TESTRXXC,
    QISKIT_RXXC,
    RESULTS_TESTRYYA,
    QISKIT_RYYA,
    RESULTS_TESTRYYB,
    QISKIT_RYYB,
    RESULTS_TESTRYYC,
    QISKIT_RYYC,
    RESULTS_TESTRZZA,
    QISKIT_RZZA,
    RESULTS_TESTRZZB,
    QISKIT_RZZB,
    RESULTS_TESTRZZC,
    QISKIT_RZZC,
    RESULTS_TESTS,
    QISKIT_S,
    RESULTS_TESTSDG,
    QISKIT_SDG,
    RESULTS_TESTSWAP,
    QISKIT_SWAP,
    RESULTS_TESTT,
    QISKIT_T,
    RESULTS_TESTTDG,
    QISKIT_TDG,
    RESULTS_TESTU,
    QISKIT_U,
    RESULTS_TESTY,
    QISKIT_Y,
    RESULTS_TESTZ,
    QISKIT_Z
)


class TestEmpty(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(send_request(EMPTY, super().qc_type))

    def test_status_code(self):
        assert self.data[STATUS] == BAD_REQUEST_ERR

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 0

    def test_circuit_dirac_little_endian(self):
        assert self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN] is None

    def test_circuit_dirac_big_endian(self):
        assert self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN] is None

    def test_dirac_state_little_endian(self):
        assert self.data[DIRAC_STATE_LITTLE_ENDIAN] is None

    def test_dirac_state_big_endian(self):
        assert self.data[DIRAC_STATE_BIG_ENDIAN] is None

    def test_matrix_gate_little_endian(self):
        assert self.data[MATRIX_GATE_LITTLE_ENDIAN] is None

    def test_matrix_gate_big_endian(self):
        assert self.data[MATRIX_GATE_BIG_ENDIAN] is None

    def test_matrix_gate_tensor_little_endian(self):
        assert self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN] is None

    def test_matrix_gate_tensor_big_endian(self):
        assert self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN] is None

    def test_matrix_state_little_endian(self):
        assert self.data[MATRIX_STATE_LITTLE_ENDIAN] is None

    def test_matrix_state_big_endian(self):
        assert self.data[MATRIX_STATE_BIG_ENDIAN] is None


class TestTypo(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(send_request(QISKIT_TYPO, super().qc_type))

    def test_status_code(self):
        assert self.data[STATUS] == BAD_REQUEST_ERR

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 0

    def test_circuit_dirac_little_endian(self):
        assert self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN] is None

    def test_circuit_dirac_big_endian(self):
        assert self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN] is None

    def test_dirac_state_little_endian(self):
        assert self.data[DIRAC_STATE_LITTLE_ENDIAN] is None

    def test_dirac_state_big_endian(self):
        assert self.data[DIRAC_STATE_BIG_ENDIAN] is None

    def test_matrix_gate_little_endian(self):
        assert self.data[MATRIX_GATE_LITTLE_ENDIAN] is None

    def test_matrix_gate_big_endian(self):
        assert self.data[MATRIX_GATE_BIG_ENDIAN] is None

    def test_matrix_gate_tensor_little_endian(self):
        assert self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN] is None

    def test_matrix_gate_tensor_big_endian(self):
        assert self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN] is None

    def test_matrix_state_little_endian(self):
        assert self.data[MATRIX_STATE_LITTLE_ENDIAN] is None

    def test_matrix_state_big_endian(self):
        assert self.data[MATRIX_STATE_BIG_ENDIAN] is None


class TestSingleQubitSingleHadamard(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_SINGLE_QUBIT_SINGLE_HADAMARD, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD[MATRIX_STATE_BIG_ENDIAN]
        )


class TestSingleColumnTwoQubitNeighbouringGate(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(
                QISKIT_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE, super().qc_type
            )
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN
            ]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                CIRCUIT_DIRAC_GATE_BIG_ENDIAN
            ]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                DIRAC_STATE_LITTLE_ENDIAN
            ]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                MATRIX_GATE_LITTLE_ENDIAN
            ]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                MATRIX_GATE_TENSOR_LITTLE_ENDIAN
            ]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                MATRIX_GATE_TENSOR_BIG_ENDIAN
            ]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                MATRIX_STATE_LITTLE_ENDIAN
            ]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE[
                MATRIX_STATE_BIG_ENDIAN
            ]
        )


class TestHigherIndexedControlQubit(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_HIGHER_CONTROL_QUBIT_INDEX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == BAD_REQUEST_ERR

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_HIGHER_CONTROL_QUBIT_INDEX[MATRIX_STATE_BIG_ENDIAN]
        )


class TestNonNeighbouringQubits(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_NON_NEIGHBOURING_QUBITS, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == BAD_REQUEST_ERR

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_NON_NEIGHBOURING_QUBITS[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_NON_NEIGHBOURING_QUBITS[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCCX(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CCX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCCX[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCCX[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCX[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCCX[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCX[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCCX[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCCX[MATRIX_STATE_BIG_ENDIAN]
        )
class TestCCZ(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CCZ, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCCZ[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCCZ[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCZ[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCCZ[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCZ[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCCZ[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCCZ[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCH(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CH, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCH[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCH[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCH[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCH[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCH[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCH[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCH[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCH[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCH[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCH[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCH[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCH[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASEA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CPHASEA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCPHASEA[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCPHASEA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEA[MATRIX_STATE_BIG_ENDIAN]
        )
class TestCPHASEB(TestQiskit):

    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CPHASEB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCPHASEB[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCPHASEB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASEC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CPHASEC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCPHASEC[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCPHASEC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASEC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRXA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRXA[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRXA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRXB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRXB[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRXB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRXC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRXC[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRXC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRXC[MATRIX_STATE_BIG_ENDIAN]
        )


class TestCRYA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRYA[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRYA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRYB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRYB[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRYB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRYC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRYC[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRYC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRZA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRZA[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRZA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRZB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRZB[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRZB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRZC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRZC[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRZC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRZC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CRZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCRZC[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCRZC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCRZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCS[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCS(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CS, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCS[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCS[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCS[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCS[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCS[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCS[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCS[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCS[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCS[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCS[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCS[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCS[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCSDG(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CSDG, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCSDG[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCSDG[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSDG[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSDG[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSDG[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSDG[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSDG[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCSWAP(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CSWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCSWAP[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCSWAP[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSWAP[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSWAP[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSWAP[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSWAP[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSWAP[MATRIX_STATE_BIG_ENDIAN]
        ) 

class TestCSX(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CSX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCSX[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCSX[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSX[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSX[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSX[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSX[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCSX[MATRIX_STATE_BIG_ENDIAN]
        )      

class TestCX(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCX[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCX[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCX[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCX[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCX[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCX[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCX[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCX[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCX[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCX[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCX[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCX[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCY(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CY, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCY[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCY[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCY[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCY[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCY[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCY[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCY[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCY[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCY[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCY[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCY[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCY[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCZ(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_CZ, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTCZ[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTCZ[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCZ[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCZ[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCZ[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCZ[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCZ[MATRIX_STATE_BIG_ENDIAN]
        )

class TestDCX(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_DCX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == RESULTS_TESTDCX[STATUS]

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTDCX[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTDCX[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTDCX[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTDCX[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTDCX[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTDCX[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISWAP(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_ISWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTISWAP[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISWAP[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISWAP[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISWAP[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISWAP[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISWAP[MATRIX_STATE_BIG_ENDIAN]
        )

class TestPHASEA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_PHASEA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTPHASEA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEA[MATRIX_STATE_BIG_ENDIAN]
        )


class TestPHASEB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_PHASEB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTPHASEB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestPHASEC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_PHASEC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTPHASEC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTPHASEC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestR(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_R, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTR[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTR[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTR[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTR[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTR[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTR[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTR[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTR[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTR[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTR[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTR[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRV(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RV, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRV[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRV[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRV[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRV[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRV[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRV[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRV[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRV[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTRV[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRV[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRV[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_STATE_BIG_ENDIAN]
        )


class TestRXXA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXXA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXXA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXXB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXXB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXXB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXXC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RXXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRXXC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRXXC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRXXC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRXXC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXXC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYYA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYYA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYYA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYYB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYYB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYYB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYYC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RYYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRYYC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRYYC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRYYC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRYYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZZA(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZZA[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZZA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZZB(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZZB[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZZB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZZC(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_RZZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTRZZC[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTRZZC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTRZZC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTRZZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZZC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestS(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_S, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTS[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTS[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTS[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTS[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTS[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTS[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTS[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTS[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTS[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTS[MATRIX_STATE_BIG_ENDIAN]
        )

class TestSDG(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_SDG, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTSDG[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTSDG[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTSDG[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTSDG[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTSDG[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTSDG[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTSDG[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTSDG[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTSDG[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTSDG[MATRIX_STATE_BIG_ENDIAN]
        )

class TestSWAP(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_SWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTSWAP[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTSWAP[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTSWAP[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTSWAP[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTSWAP[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_STATE_BIG_ENDIAN]
        )

class TestT(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_T, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTT[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTT[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTT[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTT[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTT[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTT[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTT[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTT[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTT[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTT[MATRIX_STATE_BIG_ENDIAN]
        )

class TestTDG(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_TDG, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTTDG[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTTDG[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTTDG[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTTDG[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTTDG[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTTDG[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTTDG[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTTDG[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTTDG[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTTDG[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_U, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTU[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU[MATRIX_STATE_BIG_ENDIAN]
        )

class TestY(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_Y, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTY[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTY[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTY[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTY[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTY[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTY[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTY[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTY[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTY[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTY[MATRIX_STATE_BIG_ENDIAN]
        )

class TestZ(TestQiskit):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(QISKIT_Z, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == RESULTS_TESTZ[NUM_QUBITS]

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTZ[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTZ[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTZ[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTZ[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTZ[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTZ[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTZ[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTZ[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTZ[MATRIX_STATE_BIG_ENDIAN]
        )