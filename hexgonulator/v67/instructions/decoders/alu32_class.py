from hexgonulator.common.bits_ops import substring, bit_at
from ..concrete.nop import Nop
from ..concrete.q6_r_add_ri import Q6RAddRi
from ..concrete.q6_r_add_rr import Q6RAddRr
from ..concrete.q6_r_add_rr_sat import Q6RAddRrSat
from ..concrete.q6_r_and_ri import Q6RAndRi
from ..concrete.q6_r_and_rnr import Q6RAndRnr
from ..concrete.q6_r_and_rr import Q6RAndRr
from ..concrete.q6_r_equals_i import Q6REqualsI
from ..concrete.q6_r_or_ri import Q6ROrRi
from ..concrete.q6_r_or_rnr import Q6ROrRnr
from ..concrete.q6_r_or_rr import Q6ROrRr
from ..concrete.q6_r_sub_ir import Q6RSubIr
from ..concrete.q6_r_sub_rr import Q6RSubRr
from ..concrete.q6_r_sub_rr_sat import Q6RSubRrSat
from ..concrete.q6_r_sxtb_r import Q6RSxtbR
from ..concrete.q6_r_sxth_r import Q6RSxthR
from ..concrete.q6_r_xor_rr import Q6RXorRr
from ..concrete.q6_rh_equals_i import Q6RhEqualsI
from ..concrete.q6_rl_equals_i import Q6RlEqualsI


def decode_alu_32_class(instruction):
    iclass = substring(instruction, 31, 28)
    if iclass == 0b0111:
        maj_op = substring(instruction, 26, 24)
        min_op = substring(instruction, 23, 21)
        rs = bit_at(instruction, 27)
        if maj_op == 0b110 and ((min_op >> 1) == 0b00):
            return Q6RAndRi.from_int(instruction)
        if maj_op == 0b110 and ((min_op >> 1) == 0b10):
            return Q6ROrRi.from_int(instruction)
        if maj_op == 0b111 and rs:
            return Nop.from_int(instruction)
        if maj_op == 0b110 and ((min_op >> 1) == 0b01):
            return Q6RSubIr.from_int(instruction)
        if maj_op == 0b000 and min_op == 0b101:
            return Q6RSxtbR.from_int(instruction)
        if maj_op == 0b000 and min_op == 0b111:
            return Q6RSxthR.from_int(instruction)
        if maj_op == 0b000 and rs:
            return Q6REqualsI.from_int(instruction)
        if maj_op == 0b010 and min_op & 1 == 1:
            return Q6RhEqualsI.from_int(instruction)
        if maj_op == 0b001 and min_op & 1 == 1:
            return Q6RlEqualsI.from_int(instruction)
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
        if maj_op == 0b001 and min_op == 0b011:
            return Q6RXorRr.from_int(instruction)
        if maj_op == 0b001 and min_op == 0b100:
            return Q6RAndRnr.from_int(instruction)
        if maj_op == 0b001 and min_op == 0b101:
            return Q6ROrRnr.from_int(instruction)
        if maj_op == 0b011 and min_op == 0b001:
            return Q6RSubRr.from_int(instruction)
        if maj_op == 0b110 and min_op == 0b110:
            return Q6RSubRrSat.from_int(instruction)
