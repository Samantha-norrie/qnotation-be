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
    RESULTS_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE,
    RESULTS_BELL_STATES_THREE_QUBITS,
    RESULTS_NON_NEIGHBOURING_QUBITS,
    CIRQ_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE,
    CIRQ_BELL_STATE_THREE_QUBITS,
    CIRQ_NON_NEIGHBOURING_QUBITS
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

class TestSingleColumnTwoQubitNeighbouringGate(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(
                CIRQ_SINGLE_COLUMN_TWO_QUBIT_NEIGHBOURING_GATE, super().qc_type
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

# TODO: confirm expected behaviour
class TestBellStateThreeQubits(TestCirq):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(CIRQ_BELL_STATE_THREE_QUBITS, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 3

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_BELL_STATES_THREE_QUBITS[MATRIX_STATE_BIG_ENDIAN]
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