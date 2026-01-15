import numpy as np
from quantum_library_parsers.parser_utils import GateNames

SQRT2_INV = 1 / np.sqrt(2)

gate_aliases = {
    GateNames.CONTROLLED_CONTROLLED_X.value: [
        "ccx",
        "controlled-controlled-x",
        "CCNOT",
        "toffoli"
    ],
    
    GateNames.CONTROLLED_CONTROLLED_Z.value: ["ccz", "controlled-controlled-z"],
    GateNames.CONTROLLED_HADAMARD.value: ["ch", "controlled-hadamard"],
    GateNames.CONTROLLED_PHASE.value: ["cp", "controlled-phase",
    "controlledphaseshift"],
    GateNames.CONTROLLED_PHASE_00.value: ["cp00", "controlled-phase-00", "controlledphaseshift00", "cphaseshift00"],
    GateNames.CONTROLLED_PHASE_01.value: ["cp01", "controlled-phase-00", "controlledphaseshift01", "cphaseshift01"],
    GateNames.CONTROLLED_PHASE_10.value: ["cp10", "controlled-phase-10", "controlledphaseshift10", "cphaseshift10"],
    GateNames.CONTROLLED_ROTATIONAL.value: ["crot"],
    GateNames.CONTROLLED_ROTATIONAL_X.value: [
        "crx",
        "controlled-rotational-x",
        "controlled-rotational-not",
    ],
    GateNames.CONTROLLED_ROTATIONAL_Y.value: ["cry", "controlled-rotational-Y"],
    GateNames.CONTROLLED_ROTATIONAL_Z.value: ["crz", "controlled-rotational-Z"],
    GateNames.CONTROLLED_S_DAGGER.value: ["csdg", "controlled-s-dagger"],
    GateNames.CONTROLLED_S.value: ["cs", "controlled-s"],
    GateNames.CONTROLLED_SQUARED_X.value: ["csx", "controlled-squared-x"],
    GateNames.CONTROLLED_SWAP.value: ["cswap", "controlled-swap", "fredkin"],
    GateNames.CONTROLLED_U.value: ["cu", "controlled-u", "controlled-unitary"],
    GateNames.CONTROLLED_X.value: ["cx", "cnot", "controlled-not", "controlled-x"],
    GateNames.CONTROLLED_Y.value: ["cy", "controlled-y"],
    GateNames.CONTROLLED_Z.value: ["cz", "controlled-z"],
    GateNames.ECR.value: ["ecr", "echoed-cross-resonance"],
    GateNames.DIAGONAL.value: ["d", "diagonal"],
    GateNames.DOUBLE_CONTROLLED_X.value: ["dcx", "double-controlled-x"],
    GateNames.HADAMARD.value: ["h", "hadamard"],
    GateNames.IDENTITY.value: ["i", "id", "identity"],
    GateNames.ISING_XX.value: ["isingxx", "ising-xx", "xx-interaction"],
    GateNames.ISING_XY.value: ["isingxy", "ising-xy", "xy-interaction"],
    GateNames.ISING_YY.value: ["isingyy", "ising-yy", "yy-interaction"],
    GateNames.ISING_ZZ.value: ["isingzz", "ising-zz", "zz-interaction"],
    GateNames.ISWAP.value: ["iswap", "i-swap", "iswap-gate"],
    GateNames.PHASE.value: ["p", "phase"],
    GateNames.PSWAP.value: ["pswap", "p-swap", "phase-swap", "phaseswap"],
    GateNames.RELATIVE_PHASE_CONTROLLED_CONTROLLED_X.value: [
        "rccx",
        "margolous",
        "simplified-toffoli",
    ],
    GateNames.ROTATIONAL.value: ["r", "rot", "rotational"],
    GateNames.ROTATIONAL_V.value: ["rv", "rotv", "rotational-v"],
    GateNames.ROTATIONAL_X.value: ["rx", "rot-x", "rotational-x", "rotational-not"],
    GateNames.ROTATIONAL_X_X.value: ["rxx", "rot-xx", "rotational-xx", "rotational-not-not"],
    GateNames.ROTATIONAL_Y.value: ["ry", "rot-y", "rotational-y"],
    GateNames.ROTATIONAL_Y_Y.value: ["ryy", "rot-yy", "rotational-yy"],
    GateNames.ROTATIONAL_Z.value: ["rz", "rot-z", "rotational-z"],
    GateNames.ROTATIONAL_Z_X.value: ["rzx", "rot-zx", "rotational-zx"],
    GateNames.ROTATIONAL_Z_Z.value: ["rzz", "rot-zz", "rotational-zz"],
    GateNames.SISWAP.value: ["siswap", "si-swap", "sqrt-iswap", "sqrtiswap"],
    GateNames.SWAP.value: ["swap", "sw", "swap-gate"],
    # GateNames.TOFFOLI.value: ["toffoli", "ccnot", "controlled-controlled-not"],
    GateNames.X.value: ["x", "not", "pauli-x", "paulix"],
    GateNames.X_X_MINUS_Y_Y.value: ["xx-yy"],
    GateNames.X_X_PLUS_Y_Y.value: ["xx+yy"],
    GateNames.Y.value: ["y", "pauli-y", "pauliy"],
    GateNames.Z.value: ["z", "pauli-z", "pauliz"],
}

name_to_acronym = {
    name.lower(): acronym for acronym, names in gate_aliases.items() for name in names
}


def get_gate_acronym(name: str) -> str | None:
    return name_to_acronym.get(name.lower())
