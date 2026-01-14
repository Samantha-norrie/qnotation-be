import asyncio
from .test_utils import (
    TestCirq,
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
    MATRIX_GATE_TENSOR_BIG_ENDIAN,
    MATRIX_GATE_TENSOR_LITTLE_ENDIAN,
    MATRIX_STATE_LITTLE_ENDIAN,
    MATRIX_STATE_BIG_ENDIAN,
    CIRQ_TYPO,
    CIRQ_SINGLE_QUBIT_SINGLE_HADAMARD,
    SUCCESS,
    RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD,
    RESULTS_NON_NEIGHBOURING_QUBITS,
    CIRQ_NON_NEIGHBOURING_QUBITS,
    CIRQ_CCX,
    RESULTS_TESTCCX,
    CIRQ_CCZ,
    RESULTS_TESTCCZ,
    CIRQ_CSWAP,
    RESULTS_TESTCSWAP,
    CIRQ_ISWAP,
    RESULTS_TESTISWAP,
    CIRQ_RXA,
    RESULTS_TESTRXA,
    CIRQ_RXB,
    RESULTS_TESTRXB,
    CIRQ_RXC,
    RESULTS_TESTRXC,
    CIRQ_RYA,
    RESULTS_TESTRYA,
    CIRQ_RYB,
    RESULTS_TESTRYB,
    CIRQ_RYC,
    RESULTS_TESTRYC,
    CIRQ_RZA,
    RESULTS_TESTRZA,
    CIRQ_RZB,
    RESULTS_TESTRZB,
    CIRQ_RZC,
    RESULTS_TESTRZC
)


class TestEmpty(TestCirq):
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


class TestTypo(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(send_request(CIRQ_TYPO, super().qc_type))

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


class TestSingleQubitSingleHadamard(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_SINGLE_QUBIT_SINGLE_HADAMARD, super().qc_type)
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

class TestNonNeighbouringQubits(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_NON_NEIGHBOURING_QUBITS, super().qc_type)
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

class TestCCX(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_CCX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

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

class TestCCZ(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_CCZ, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

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

class TestCSWAP(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_CSWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

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

class TestISWAP(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_ISWAP, super().qc_type)
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

class TestRXA(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RXA, super().qc_type)
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
            == RESULTS_TESTRXA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRXB(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RXB, super().qc_type)
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
            == RESULTS_TESTRXB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRXC(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RXC, super().qc_type)
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
            == RESULTS_TESTRXC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRYA(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RYA, super().qc_type)
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
            == RESULTS_TESTRYA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRYB(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RYB, super().qc_type)
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
            == RESULTS_TESTRYB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRYC(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RYC, super().qc_type)
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
            == RESULTS_TESTRYC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRZA(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RZA, super().qc_type)
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
            == RESULTS_TESTRZA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRZB(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RZB, super().qc_type)
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
            == RESULTS_TESTRZB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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

class TestRZC(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_RZC, super().qc_type)
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
            == RESULTS_TESTRZC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
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