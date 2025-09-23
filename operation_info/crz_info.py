import numpy as np
import cmath
from .multi_qubit_matrix_information import MultiQubitMatrixInformation


class CRZInfo(MultiQubitMatrixInformation):
    names = ["crz", "controlled-rotational-z", "controlled-rz"]

    def get_big_endian(self, params):
        theta = params.theta
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, cmath.exp(-1j * theta / 2), 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, cmath.exp(1j * theta / 2)],
            ],
            dtype=complex,
        )

    def get_little_endian(self, params):
        theta = params.theta
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, cmath.exp(-1j * theta / 2), 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, cmath.exp(1j * theta / 2)],
            ],
            dtype=complex,
        )
