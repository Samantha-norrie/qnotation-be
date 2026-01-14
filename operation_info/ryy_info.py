import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class RYYInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ROTATIONAL_Y_Y.value]

    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, 0, 0, -s],
            [0, c, s, 0],
            [0, s, c, 0],
            [-s, 0, 0, c]
        ], dtype=complex)


    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        c = np.cos(theta / 2)
        s = np.sin(theta / 2)
        return np.array([
            [c, 0, 0, -s],
            [0, c, s, 0],
            [0, s, c, 0],
            [-s, 0, 0, c]
        ], dtype=complex)