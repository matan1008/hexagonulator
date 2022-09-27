from hexgonulator.common.bits_ops import substring
from ..concrete.q6_r_add_ri import Q6RAddRi
from ..concrete.q6_r_add_rr import Q6RAddRr
from ..concrete.q6_r_add_rr_sat import Q6RAddRrSat
from ..concrete.q6_r_and_ri import Q6RAndRi
from ..concrete.q6_r_and_rr import Q6RAndRr
from ..concrete.q6_r_or_ri import Q6ROrRi
from ..concrete.q6_r_or_rr import Q6ROrRr


def decode_alu_32_class(instruction):
    iclass = substring(instruction, 31, 28)
    if iclass == 0b0111:
        maj_op = substring(instruction, 26, 24)
        min_op = substring(instruction, 23, 21)
        if maj_op == 0b110 and ((min_op >> 1) == 0b00):
            return Q6RAndRi.from_int(instruction)
        if maj_op == 0b110 and ((min_op >> 1) == 0b10):
            return Q6ROrRi.from_int(instruction)
    elif iclass == 0b1011:
        return Q6RAddRi.from_int(instruction)
    elif iclass == 0b1111:
        maj_op = substring(instruction, 26, 24)
        min_op = substring(instruction, 23, 21)
        if maj_op == 0b011 and min_op == 0b000:
            return Q6RAddRr.from_int(instruction)
        if maj_op == 0b110 and min_op == 0b010:
            return Q6RAddRrSat.from_int(instruction)
        if maj_op == 0b001 and min_op == 0b000:
            return Q6RAndRr.from_int(instruction)
        if maj_op == 0b001 and min_op == 0b001:
            return Q6ROrRr.from_int(instruction)
