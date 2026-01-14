import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class RZZInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ROTATIONAL_Z_Z.value]

    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        a = np.exp(-1j * theta / 2)
        b = np.exp( 1j * theta / 2)
        return np.array([
            [a, 0, 0, 0],
            [0, b, 0, 0],
            [0, 0, b, 0],
            [0, 0, 0, a]
        ], dtype=complex)


    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        a = np.exp(-1j * theta / 2)
        b = np.exp( 1j * theta / 2)
        return np.array([
            [a, 0, 0, 0],
            [0, b, 0, 0],
            [0, 0, b, 0],
            [0, 0, 0, a]
        ], dtype=complex)