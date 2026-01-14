import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from .operation_info_utils import SQRT2_INV
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class CHInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.CONTROLLED_HADAMARD.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, SQRT2_INV, SQRT2_INV],
                [0.0 + 0.0j, 0.0 + 0.0j, SQRT2_INV, -SQRT2_INV],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, SQRT2_INV, 0.0 + 0.0j, SQRT2_INV],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0, 0.0 + 0.0j],
                [0.0 + 0.0j, SQRT2_INV, 0.0 + 0.0j, -SQRT2_INV],
            ],
            dtype=complex,
        )
