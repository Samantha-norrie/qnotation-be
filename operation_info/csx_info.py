import numpy as np
from .multi_qubit_matrix_information import MultiQubitMatrixInformation
from quantum_library_parsers.parser_utils import GateNames
from .operation_info_utils import gate_aliases

class CSXInfo(MultiQubitMatrixInformation):
    names = gate_aliases[GateNames.CONTROLLED_SQUARED_X.value]

    @staticmethod
    def get_big_endian():
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, 0.0 + 0.0j, (1 + 1j)/2, (1 - 1j)/2],
                [0.0 + 0.0j, 0.0 + 0.0j, (1 - 1j)/2, (1 + 1j)/2],
            ],
            dtype=complex,
        )

    @staticmethod
    def get_little_endian():
        return np.array(
            [
                [1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, (1 + 1j)/2, 0.0 + 0.0j, (1 - 1j)/2],
                [0.0 + 0.0j, 0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j],
                [0.0 + 0.0j, (1 - 1j)/2, 0.0 + 0.0j, (1 + 1j)/2],
            ],
            dtype=complex,
        )