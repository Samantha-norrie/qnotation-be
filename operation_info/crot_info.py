import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class CROTInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.CONTROLLED_ROTATIONAL.value]

    @staticmethod
    def get_big_endian(params):
        phi = params[0]
        theta = params[1]
        omega = params[2]

        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    cmath.exp(-1j *(phi + omega))*cmath.cos(theta / 2),
                    -cmath.exp(1j *(phi - omega))*cmath.sin(theta / 2),
                ],
                [
                    0.0 + 0.0j,
                    0.0 + 0.0j,
                    -cmath.exp(-1j *(phi - omega))*cmath.sin(theta / 2),
                    cmath.exp(1j *(phi + omega))*cmath.cos(theta / 2),
                ],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian(params):
        phi = params[0]
        theta = params[1]
        omega = params[2]

        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    cmath.exp(-1j *(phi + omega))*cmath.cos(theta / 2),
                    0.0 + 0.0j,
                    -cmath.exp(1j *(phi - omega))*cmath.sin(theta / 2),
                ],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
                [
                    0.0 + 0.0j,
                    -cmath.exp(-1j *(phi - omega))*cmath.sin(theta / 2),
                    0.0 + 0.0j,
                    cmath.exp(1j *(phi + omega))*cmath.cos(theta / 2),
                ],
            ],
            dtype=complex,
        )