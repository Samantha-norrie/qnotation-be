import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class DCXInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.DOUBLE_CONTROLLED_X.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]], dtype=complex
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [[1, 0, 0, 0], [0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0]], dtype=complex
        )