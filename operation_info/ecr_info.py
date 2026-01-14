import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases, SQRT2_INV

class ECRInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ECR.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [[0, 0, SQRT2_INV, SQRT2_INV*1j], [0, 0, SQRT2_INV*1j, SQRT2_INV], [SQRT2_INV, SQRT2_INV*-1j, 0, 0], [SQRT2_INV*-1j, SQRT2_INV, 0, 0]], dtype=complex
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [[0, SQRT2_INV, 0, SQRT2_INV*1j], [SQRT2_INV, 0, SQRT2_INV*1j, 0], [0, SQRT2_INV*-1j, 0, SQRT2_INV], [SQRT2_INV*-1j, 0, SQRT2_INV, 0]], dtype=complex
        )