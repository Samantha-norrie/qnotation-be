import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class PSWAPInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.PSWAP.value]

    @staticmethod
    def get_big_endian(params):
        phi = params[0]
        return np.array(
            [[1, 0, 0, 0], [0, 0, cmath.exp(1j*phi), 0], [0, cmath.exp(1j*phi), 0, 0], [0, 0, 0, 1]], dtype=complex
        )

    @staticmethod
    def get_big_endian(params):
        phi = params[0]
        return np.array(
            [[1, 0, 0, 0], [0, 0, cmath.exp(1j*phi), 0], [0, cmath.exp(1j*phi), 0, 0], [0, 0, 0, 1]], dtype=complex
        )