import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases, SQRT2_INV

class SISWAPInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.SISWAP.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [[1, 0, 0, 0], [0, SQRT2_INV, 1j*SQRT2_INV, 0], [0, 1j*SQRT2_INV, SQRT2_INV, 0], [0, 0, 0, 1]], dtype=complex
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [[1, 0, 0, 0], [0, SQRT2_INV, 1j*SQRT2_INV, 0], [0, 1j*SQRT2_INV, SQRT2_INV, 0], [0, 0, 0, 1]], dtype=complex
        )