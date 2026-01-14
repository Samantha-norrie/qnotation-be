import numpy as np
import math
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class ISINGXXInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.ISING_XX.value]

    @staticmethod
    def get_big_endian(params):
        phi = params[0]
        return np.array(
            [
                [cmath.cos(phi/2) + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, -1j*cmath.sin(phi/2)],
                [0.0 + 0.0j, cmath.cos(phi/2) + 0.0j, -1j*cmath.sin(phi/2), 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    -1j*cmath.sin(phi/2),
                    cmath.cos(phi/2) + 0.0j,
                    0.0 + 0.0j,
                ],
                [
                    -1j*cmath.sin(phi/2),
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    cmath.cos(phi/2)
                ],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian(params):
        phi = params[0]
        return np.array(
            [
                [cmath.cos(phi/2) + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, -1j*cmath.sin(phi/2)],
                [0.0 + 0.0j, cmath.cos(phi/2) + 0.0j, -1j*cmath.sin(phi/2), 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    -1j*cmath.sin(phi/2),
                    cmath.cos(phi/2) + 0.0j,
                    0.0 + 0.0j,
                ],
                [
                    -1j*cmath.sin(phi/2),
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    cmath.cos(phi/2)
                ],
            ],
            dtype=complex,
        )
