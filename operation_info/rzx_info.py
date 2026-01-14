import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class RZXInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ROTATIONAL_Z_X.value]

    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, -1j*s, 0, 0],
            [-1j*s, c, 0, 0],
            [0, 0, c, 1j*s],
            [0, 0, 1j*s, c]
        ], dtype=complex)


    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, -1j*s, 0, 0],
            [-1j*s, c, 0, 0],
            [0, 0, c, 1j*s],
            [0, 0, 1j*s, c]
        ], dtype=complex)