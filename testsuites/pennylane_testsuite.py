import asyncio
from .test_utils import (
    TestPennylane,
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
    PENNYLANE_TYPO,
    SUCCESS,
    RESULTS_SINGLE_QUBIT_SINGLE_HADAMARD,
    PENNYLANE_EMPTY,
    PENNYLANE_TYPO,
    PENNYLANE_NON_NEIGHBOURING_QUBITS,
    RESULTS_NON_NEIGHBOURING_QUBITS,
    PENNYLANE_HIGHER_CONTROL_QUBIT,
    PENNYLANE_CCX,
    RESULTS_TESTCCX,
    PENNYLANE_CH,
    RESULTS_TESTCH,
    PENNYLANE_CPHASEA,
    RESULTS_TESTCPHASEA,
    PENNYLANE_CPHASEB,
    RESULTS_TESTCPHASEB,
    PENNYLANE_CPHASEC,
    RESULTS_TESTCPHASEC,
    PENNYLANE_CPHASESHIFT00A,
    RESULTS_TESTCPHASESHIFT00A,
    PENNYLANE_CPHASESHIFT00B,
    RESULTS_TESTCPHASESHIFT00B,
    PENNYLANE_CPHASESHIFT00C,
    RESULTS_TESTCPHASESHIFT00C,
    PENNYLANE_CPHASESHIFT01A,
    RESULTS_TESTCPHASESHIFT01A,
    PENNYLANE_CPHASESHIFT01B,
    RESULTS_TESTCPHASESHIFT01B,
    PENNYLANE_CPHASESHIFT01C,
    RESULTS_TESTCPHASESHIFT01C,
    PENNYLANE_CPHASESHIFT10A,
    RESULTS_TESTCPHASESHIFT10A,
    PENNYLANE_CPHASESHIFT10B,
    RESULTS_TESTCPHASESHIFT10B,
    PENNYLANE_CPHASESHIFT10C,
    RESULTS_TESTCPHASESHIFT10C,
    PENNYLANE_CROT,
    RESULTS_TESTCROT,
    PENNYLANE_CRXA,
    RESULTS_TESTCRXA,
    PENNYLANE_CRXB,
    RESULTS_TESTCRXB,
    PENNYLANE_CRXC,
    RESULTS_TESTCRXC,
    PENNYLANE_CRYA,
    RESULTS_TESTCRYA,
    PENNYLANE_CRYB,
    RESULTS_TESTCRYB,
    PENNYLANE_CRYC,
    RESULTS_TESTCRYC,
    PENNYLANE_CRZA,
    RESULTS_TESTCRZA,
    PENNYLANE_CRZB,
    RESULTS_TESTCRZB,
    PENNYLANE_CRZC,
    RESULTS_TESTCRZC,
    PENNYLANE_CSWAP,
    RESULTS_TESTCSWAP,
    PENNYLANE_CX,
    RESULTS_TESTCX,
    PENNYLANE_CY,
    RESULTS_TESTCY,
    PENNYLANE_CZ,
    RESULTS_TESTCZ,
    PENNYLANE_ISINGXXA,
    RESULTS_TESTISINGXXA,
    PENNYLANE_ISINGXXB,
    RESULTS_TESTISINGXXB,
    PENNYLANE_ISINGXXC,
    RESULTS_TESTISINGXXC,
    PENNYLANE_ISINGXYA,
    RESULTS_TESTISINGXYA,
    PENNYLANE_ISINGXYB,
    RESULTS_TESTISINGXYB,
    PENNYLANE_ISINGXYC,
    RESULTS_TESTISINGXYC,
    PENNYLANE_ISINGYYA,
    RESULTS_TESTISINGYYA,
    PENNYLANE_ISINGYYB,
    RESULTS_TESTISINGYYB,
    PENNYLANE_ISINGYYC,
    RESULTS_TESTISINGYYC,
    PENNYLANE_ISINGZZA,
    RESULTS_TESTISINGZZA,
    PENNYLANE_ISINGZZB,
    RESULTS_TESTISINGZZB,
    PENNYLANE_ISINGZZC,
    RESULTS_TESTISINGZZC,
    PENNYLANE_R,
    RESULTS_TESTR,
    PENNYLANE_RXA,
    RESULTS_TESTRXA,
    PENNYLANE_RXB,
    RESULTS_TESTRXB,
    PENNYLANE_RXC,
    RESULTS_TESTRXC,
    PENNYLANE_RYA,
    RESULTS_TESTRYA,
    PENNYLANE_RYB,
    RESULTS_TESTRYB,
    PENNYLANE_RYC,
    RESULTS_TESTRYC,
    PENNYLANE_RZA,
    RESULTS_TESTRZA,
    PENNYLANE_RZB,
    RESULTS_TESTRZB,
    PENNYLANE_RZC,
    RESULTS_TESTRZC,
    PENNYLANE_S,
    RESULTS_TESTS,
    PENNYLANE_SWAP,
    RESULTS_TESTSWAP,
    PENNYLANE_U3,
    RESULTS_TESTU3,
    PENNYLANE_U1A,
    RESULTS_TESTU1A,
    PENNYLANE_U1B,
    RESULTS_TESTU1B,
    PENNYLANE_U1C,
    RESULTS_TESTU1C,
    PENNYLANE_U2A,
    RESULTS_TESTU2A,
    PENNYLANE_U2B,
    RESULTS_TESTU2B,
    PENNYLANE_Y,
    RESULTS_TESTY,
    PENNYLANE_Z,
    RESULTS_TESTZ
    )


class TestEmpty(TestPennylane):
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


class TestTypo(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(send_request(PENNYLANE_TYPO, super().qc_type))

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

class TestCCX(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CCX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 3

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

class TestCH(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CH, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCPHASEA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASEA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCPHASEB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASEB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCPHASEC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASEC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCPHASESHIFT00A(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT00A, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00A[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT00B(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT00B, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00B[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT00C(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT00C, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT00C[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT01A(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT01A, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01A[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT01B(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT01B, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01B[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT01C(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT01C, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT01C[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT10A(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT10A, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10A[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT10B(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT10B, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10B[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCPHASESHIFT10C(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CPHASESHIFT10C, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCPHASESHIFT10C[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCROT(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CROT, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCROT[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTCROT[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCROT[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTCROT[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTCROT[MATRIX_STATE_BIG_ENDIAN]
        )

class TestCRXA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRXB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRXC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRYA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRYB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRYC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRZA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRZB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCRZC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CRZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCSWAP(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CSWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 3

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

class TestCX(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CX, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCY(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CY, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestCZ(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_CZ, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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

class TestISINGXXA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGXXB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGXXC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXXC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGXYA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGXYB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGXYC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGXYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGXYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGYYA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGYYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGYYB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGYYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGYYC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGYYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGYYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGZZA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGZZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZA[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZA[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZA[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZA[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestISINGZZB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGZZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZB[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZB[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZB[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZB[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZB[MATRIX_STATE_BIG_ENDIAN]
        )


class TestISINGZZC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_ISINGZZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZC[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZC[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZC[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZC[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_GATE_TENSOR_BIG_ENDIAN]
        )

    def test_matrix_state_little_endian(self):
        assert (
            self.data[MATRIX_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTISINGZZC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestR(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_R, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTISINGZZC[DIRAC_STATE_LITTLE_ENDIAN]
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

class TestRXA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RXA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRXA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RXB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRXB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRXC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RXC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRXC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRXC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RYA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRYA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RYB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRYB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRYC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RYC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRYC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRYC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZA(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RZA, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRZA[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZA[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZB(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RZB, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRZB[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZB[MATRIX_STATE_BIG_ENDIAN]
        )

class TestRZC(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_RZC, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTRZC[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTRZC[MATRIX_STATE_BIG_ENDIAN]
        )

class TestS(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_S, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTS[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTS[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTS[MATRIX_STATE_BIG_ENDIAN]
        )

class TestSWAP(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_SWAP, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

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
            == RESULTS_TESTSWAP[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTSWAP[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU3(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U3, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU3[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU3[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU3[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU3[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU3[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU3[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU3[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU3[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU3[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU1A(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U1A, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1A[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1A[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1A[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1A[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1A[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1A[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU1A[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU1A[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1A[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU1B(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U1B, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1B[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1B[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1B[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1B[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1B[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1B[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU1B[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU1B[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1B[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU1C(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U1C, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1C[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1C[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1C[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1C[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU1C[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU1C[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU1C[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU1C[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU1C[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU2A(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U2A, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2A[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU2A[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2A[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU2A[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2A[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU2A[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU2A[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU2A[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU2A[MATRIX_STATE_BIG_ENDIAN]
        )

class TestU2B(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_U2B, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 2

    def test_circuit_dirac_little_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2B[CIRCUIT_DIRAC_GATE_LITTLE_ENDIAN]
        )

    def test_circuit_dirac_big_endian(self):
        assert (
            self.data[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
            == RESULTS_TESTU2B[CIRCUIT_DIRAC_GATE_BIG_ENDIAN]
        )

    def test_dirac_state_little_endian(self):
        assert (
            self.data[DIRAC_STATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2B[DIRAC_STATE_LITTLE_ENDIAN]
        )

    def test_dirac_state_big_endian(self):
        assert (
            self.data[DIRAC_STATE_BIG_ENDIAN]
            == RESULTS_TESTU2B[DIRAC_STATE_BIG_ENDIAN]
        )

    def test_matrix_gate_little_endian(self):
        assert (
            self.data[MATRIX_GATE_LITTLE_ENDIAN]
            == RESULTS_TESTU2B[MATRIX_GATE_LITTLE_ENDIAN]
        )

    def test_matrix_gate_big_endian(self):
        assert (
            self.data[MATRIX_GATE_BIG_ENDIAN]
            == RESULTS_TESTU2B[MATRIX_GATE_BIG_ENDIAN]
        )

    def test_matrix_gate_tensor_little_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
            == RESULTS_TESTU2B[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTU2B[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTU2B[MATRIX_STATE_BIG_ENDIAN]
        )

class TestY(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_Y, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTY[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTY[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTY[MATRIX_STATE_BIG_ENDIAN]
        )

class TestZ(TestPennylane):
    @classmethod
    def setup_class(cls):
        cls.data = asyncio.run(
            send_request(PENNYLANE_Z, super().qc_type)
        )

    def test_status_code(self):
        assert self.data["status"] == SUCCESS

    def test_num_qubits(self):
        assert self.data[NUM_QUBITS] == 1

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
            == RESULTS_TESTZ[MATRIX_GATE_TENSOR_LITTLE_ENDIAN]
        )

    def test_matrix_gate_tensor_big_endian(self):
        assert (
            self.data[MATRIX_GATE_TENSOR_BIG_ENDIAN]
            == RESULTS_TESTZ[MATRIX_STATE_LITTLE_ENDIAN]
        )

    def test_matrix_state_big_endian(self):
        assert (
            self.data[MATRIX_STATE_BIG_ENDIAN]
            == RESULTS_TESTZ[MATRIX_STATE_BIG_ENDIAN]
        )