import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class ISWAPInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ISWAP.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]], dtype=complex
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [[1, 0, 0, 0], [0, 0, 1j, 0], [0, 1j, 0, 0], [0, 0, 0, 1]], dtype=complex
        )