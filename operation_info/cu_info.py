import numpy as np
import math
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class CUInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.CONTROLLED_U.value]

    @staticmethod
    def get_big_endian(params):
        theta = params[0]
        phi = params[1]
        lam = params[2]
        gamma = params[3]
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    cmath.exp(1j * gamma) * math.cos(theta / 2),
                    -cmath.exp(1j * (lam + gamma)) * math.sin(theta / 2),
                ],
                [
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    cmath.exp(1j * (phi + gamma)) * math.sin(theta / 2),
                    cmath.exp(1j * (phi + lam + gamma)) * math.cos(theta / 2),
                ],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian(params):
        theta = params[0]
        phi = params[1]
        lam = params[2]
        gamma = params[3]
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    cmath.exp(1j * gamma) * math.cos(theta / 2),
                    0.0 + 0.0j,
                    -cmath.exp(1j * (lam + gamma)) * math.sin(theta / 2),
                ],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    cmath.exp(1j * (phi + gamma)) * math.sin(theta / 2),
                    0.0 + 0.0j,
                    cmath.exp(1j * (phi + lam + gamma)) * math.cos(theta / 2),
                ],
            ],
            dtype=complex,
        )
