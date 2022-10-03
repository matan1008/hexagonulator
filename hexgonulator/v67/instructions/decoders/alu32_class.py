from hexgonulator.common.bits_ops import substring, bit_at
from ..concrete.conditional_add_imm import ConditionalAddImm
from ..concrete.conditional_add_new_imm import ConditionalAddNewImm
from ..concrete.conditional_add_new_reg import ConditionalAddNewReg
from ..concrete.conditional_add_not_imm import ConditionalAddNotImm
from ..concrete.conditional_add_not_new_imm import ConditionalAddNotNewImm
from ..concrete.conditional_add_not_new_reg import ConditionalAddNotNewReg
from ..concrete.conditional_add_not_reg import ConditionalAddNotReg
from ..concrete.conditional_add_reg import ConditionalAddReg
from ..concrete.conditional_aslh import ConditionalAslh
from ..concrete.conditional_aslh_new import ConditionalAslhNew
from ..concrete.conditional_aslh_not import ConditionalAslhNot
from ..concrete.conditional_aslh_not_new import ConditionalAslhNotNew
from ..concrete.conditional_asrh import ConditionalAsrh
from ..concrete.conditional_asrh_new import ConditionalAsrhNew
from ..concrete.conditional_asrh_not import ConditionalAsrhNot
from ..concrete.conditional_asrh_not_new import ConditionalAsrhNotNew
from ..concrete.nop import Nop
from ..concrete.q6_p_combine_ii import Q6PCombineIi
from ..concrete.q6_p_combine_ii_unsigned import Q6PCombineIiUnsigned
from ..concrete.q6_p_combine_ir import Q6PCombineIr
from ..concrete.q6_p_combine_ri import Q6PCombineRi
from ..concrete.q6_p_combine_rr import Q6PCombineRr
from ..concrete.q6_p_packhl_rr import Q6PPackhlRr
from ..concrete.q6_r_add_ri import Q6RAddRi
from ..concrete.q6_r_add_rr import Q6RAddRr
from ..concrete.q6_r_add_rr_sat import Q6RAddRrSat
from ..concrete.q6_r_and_ri import Q6RAndRi
from ..concrete.q6_r_and_rnr import Q6RAndRnr
from ..concrete.q6_r_and_rr import Q6RAndRr
from ..concrete.q6_r_aslh_r import Q6RAslhR
from ..concrete.q6_r_asrh_r import Q6RAsrhR
from ..concrete.q6_r_combine_rhrh import Q6RCombineRhrh
from ..concrete.q6_r_combine_rhrl import Q6RCombineRhrl
from ..concrete.q6_r_combine_rlrh import Q6RCombineRlrh
from ..concrete.q6_r_combine_rlrl import Q6RCombineRlrl
from ..concrete.q6_r_equals_i import Q6REqualsI
from ..concrete.q6_r_equals_r import Q6REqualsR
from ..concrete.q6_r_mux_pii import Q6RMuxPii
from ..concrete.q6_r_mux_pir import Q6RMuxPir
from ..concrete.q6_r_mux_pri import Q6RMuxPri
from ..concrete.q6_r_mux_prr import Q6RMuxPrr
from ..concrete.q6_r_or_ri import Q6ROrRi
from ..concrete.q6_r_or_rnr import Q6ROrRnr
from ..concrete.q6_r_or_rr import Q6ROrRr
from ..concrete.q6_r_sub_ir import Q6RSubIr
from ..concrete.q6_r_sub_rr import Q6RSubRr
from ..concrete.q6_r_sub_rr_sat import Q6RSubRrSat
from ..concrete.q6_r_sxtb_r import Q6RSxtbR
from ..concrete.q6_r_sxth_r import Q6RSxthR
from ..concrete.q6_r_vaddh_rr import Q6RVaddhRr
from ..concrete.q6_r_vaddh_rr_sat import Q6RVaddhRrSat
from ..concrete.q6_r_vadduh_rr_sat import Q6RVadduhRrSat
from ..concrete.q6_r_vavgh_rr import Q6RVavghRr
from ..concrete.q6_r_vavgh_rr_rnd import Q6RVavghRrRnd
from ..concrete.q6_r_vnavgh_rr import Q6RVnavghRrRnd
from ..concrete.q6_r_vsubh_rr import Q6RVsubhRr
from ..concrete.q6_r_vsubh_rr_sat import Q6RVsubhRrSat
from ..concrete.q6_r_vsubuh_rr_sat import Q6RVsubuhRrSat
from ..concrete.q6_r_xor_rr import Q6RXorRr
from ..concrete.q6_r_zxth_r import Q6RZxthR
from ..concrete.q6_rh_equals_i import Q6RhEqualsI
from ..concrete.q6_rl_equals_i import Q6RlEqualsI


def decode_alu_32_class(instruction):
    iclass = substring(instruction, 31, 28)
    if iclass == 0b0111:
        maj_op = substring(instruction, 26, 24)
        min_op = substring(instruction, 23, 21)
        rs = bit_at(instruction, 27)
        bit_13 = bit_at(instruction, 13)
        if maj_op == 0b110 and ((min_op >> 1) == 0b00):
            return Q6RAndRi
        if maj_op == 0b110 and ((min_op >> 1) == 0b10):
            return Q6ROrRi
        if maj_op == 0b111 and rs:
            return Nop
        if maj_op == 0b110 and ((min_op >> 1) == 0b01):
            return Q6RSubIr
        if maj_op == 0b000 and min_op == 0b101:
            return Q6RSxtbR
        if maj_op == 0b000 and min_op == 0b111:
            return Q6RSxthR
        if maj_op == 0b000 and rs:
            return Q6REqualsI
        if not rs and maj_op == 0b010 and min_op & 1 == 1:
            return Q6RhEqualsI
        if not rs and maj_op == 0b001 and min_op & 1 == 1:
            return Q6RlEqualsI
        if not rs and maj_op == 0b000 and min_op == 0b011:
            return Q6REqualsR
        if maj_op == 0b000 and min_op == 0b110:
            return Q6RZxthR
        if rs and maj_op == 0b100 and ((min_op >> 2) == 0b0):
            return Q6PCombineIi
        if rs and maj_op == 0b100 and ((min_op >> 2) == 0b1):
            return Q6PCombineIiUnsigned
        if not rs and maj_op == 0b011 and ((min_op & 3) == 0b01) and bit_13:
            return Q6PCombineIr
        if not rs and maj_op == 0b011 and ((min_op & 3) == 0b00) and bit_13:
            return Q6PCombineRi
        if rs and (maj_op >> 1) == 0b01:
            return Q6RMuxPii
        if not rs and maj_op == 0b011 and bit_at(instruction, 23) and not bit_13:
            return Q6RMuxPir
        if not rs and maj_op == 0b011 and not bit_at(instruction, 23) and not bit_13:
            return Q6RMuxPri
        if not rs and maj_op == 0b000 and min_op == 0b000 and not bit_13:
            return Q6RAslhR
        if not rs and maj_op == 0b000 and min_op == 0b001 and not bit_13:
            return Q6RAsrhR
        if not rs and maj_op == 0b100 and ((min_op >> 2) == 0b0) and not bit_13:
            return ConditionalAddImm
        if not rs and maj_op == 0b100 and ((min_op >> 2) == 0b0) and bit_13:
            return ConditionalAddNewImm
        if not rs and maj_op == 0b100 and ((min_op >> 2) == 0b1) and not bit_13:
            return ConditionalAddNotImm
        if not rs and maj_op == 0b100 and ((min_op >> 2) == 0b1) and bit_13:
            return ConditionalAddNotNewImm
        if not rs and maj_op == 0b000 and min_op == 0b000 and bit_13 and substring(instruction, 11, 10) == 0b00:
            return ConditionalAslh
        if not rs and maj_op == 0b000 and min_op == 0b000 and bit_13 and substring(instruction, 11, 10) == 0b01:
            return ConditionalAslhNew
        if not rs and maj_op == 0b000 and min_op == 0b000 and bit_13 and substring(instruction, 11, 10) == 0b10:
            return ConditionalAslhNot
        if not rs and maj_op == 0b000 and min_op == 0b000 and bit_13 and substring(instruction, 11, 10) == 0b11:
            return ConditionalAslhNotNew
        if not rs and maj_op == 0b000 and min_op == 0b001 and bit_13 and substring(instruction, 11, 10) == 0b00:
            return ConditionalAsrh
        if not rs and maj_op == 0b000 and min_op == 0b001 and bit_13 and substring(instruction, 11, 10) == 0b01:
            return ConditionalAsrhNew
        if not rs and maj_op == 0b000 and min_op == 0b001 and bit_13 and substring(instruction, 11, 10) == 0b10:
            return ConditionalAsrhNot
        if not rs and maj_op == 0b000 and min_op == 0b001 and bit_13 and substring(instruction, 11, 10) == 0b11:
            return ConditionalAsrhNotNew
    elif iclass == 0b1011:
        return Q6RAddRi
    elif iclass == 0b1111:
        maj_op = substring(instruction, 26, 24)
        min_op = substring(instruction, 23, 21)
        p = bit_at(instruction, 27)
        if not p and maj_op == 0b011 and min_op == 0b000:
            return Q6RAddRr
        if not p and maj_op == 0b110 and min_op == 0b010:
            return Q6RAddRrSat
        if maj_op == 0b001 and min_op == 0b000:
            return Q6RAndRr
        if maj_op == 0b001 and min_op == 0b001:
            return Q6ROrRr
        if maj_op == 0b001 and min_op == 0b011:
            return Q6RXorRr
        if maj_op == 0b001 and min_op == 0b100:
            return Q6RAndRnr
        if maj_op == 0b001 and min_op == 0b101:
            return Q6ROrRnr
        if maj_op == 0b011 and min_op == 0b001:
            return Q6RSubRr
        if maj_op == 0b110 and min_op == 0b110:
            return Q6RSubRrSat
        if maj_op == 0b110 and min_op == 0b000:
            return Q6RVaddhRr
        if maj_op == 0b110 and min_op == 0b001:
            return Q6RVaddhRrSat
        if maj_op == 0b110 and min_op == 0b011:
            return Q6RVadduhRrSat
        if maj_op == 0b111 and min_op == 0b000:
            return Q6RVavghRr
        if maj_op == 0b111 and min_op == 0b001:
            return Q6RVavghRrRnd
        if maj_op == 0b111 and min_op == 0b011:
            return Q6RVnavghRrRnd
        if maj_op == 0b110 and min_op == 0b100:
            return Q6RVsubhRr
        if maj_op == 0b110 and min_op == 0b101:
            return Q6RVsubhRrSat
        if maj_op == 0b110 and min_op == 0b111:
            return Q6RVsubuhRrSat
        if maj_op == 0b011 and min_op == 0b100:
            return Q6RCombineRhrh
        if maj_op == 0b011 and min_op == 0b101:
            return Q6RCombineRhrl
        if maj_op == 0b011 and min_op == 0b110:
            return Q6RCombineRlrh
        if maj_op == 0b011 and min_op == 0b111:
            return Q6RCombineRlrl
        if maj_op == 0b101 and ((min_op >> 2) == 0b0):
            return Q6PCombineRr
        if maj_op == 0b100:
            return Q6RMuxPrr
        if maj_op == 0b101 and ((min_op >> 2) == 0b1):
            return Q6PPackhlRr
        if p and maj_op == 0b011 and min_op == 0b000 and not bit_at(instruction, 13) and not bit_at(instruction, 7):
            return ConditionalAddReg
        if p and maj_op == 0b011 and min_op == 0b000 and not bit_at(instruction, 13) and bit_at(instruction, 7):
            return ConditionalAddNotReg
        if p and maj_op == 0b011 and min_op == 0b000 and bit_at(instruction, 13) and not bit_at(instruction, 7):
            return ConditionalAddNewReg
        if p and maj_op == 0b011 and min_op == 0b000 and bit_at(instruction, 13) and bit_at(instruction, 7):
            return ConditionalAddNotNewReg
