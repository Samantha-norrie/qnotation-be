import numpy as np
import math
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class CRYInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.CONTROLLED_ROTATIONAL_Y.value]

    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, math.cos(theta / 2), -math.sin(theta / 2)],
                [0.0 + 0.0j, 0.0 + 0.0j, math.sin(theta / 2), math.cos(theta / 2)],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian(params):
        theta = params[0]
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, math.cos(theta / 2), 0.0 + 0.0j, -math.sin(theta / 2)],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, math.sin(theta / 2), 0.0 + 0.0j, math.cos(theta / 2)],
            ],
            dtype=complex,
        )
