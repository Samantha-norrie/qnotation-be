# import numpy as np
# import cmath
# from .multi_qubit_matrix_information import MultiQubitMatrixInformation
# from quantum_library_parsers.parser_utils import GateNames
# from .operation_info_utils import gate_aliases

# class CCXPOWInfo(MultiQubitMatrixInformation):
#     names = gate_aliases[GateNames.CONTROLLED_CONTROLLED_POW_X.value]

#     @staticmethod
#     def get_big_endian(params):
#         exponent = params[0]
#         global_shift = params[1]
#         return np.array(
#             [
#                 [
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     1.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     cmath.exp(1j * phi),
#                     cmath.exp(1j * phi),
#                 ],
#                 [
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     0.0 + 0.0j,
#                     cmath.exp(1j * phi),
#                     cmath.exp(1j * phi),
#                 ],
#             ],
#             dtype=complex,
#         )

#     @staticmethod
#     def get_little_endian(params):
#         exponent = params[0]
#         return np.array(
#             [
#                 [1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
#                 [0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
#                 [0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
#                 [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j],
#                 [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
#                 [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j],
#                 [0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j],
#                 [0 + 0j, 0 + 0j, 0 + 0j, 1 + 0j, 0 + 0j, 0 + 0j, 0 + 0j, 0 + 0j],
#             ],
#             dtype=complex,
#         )