from hexgonulator.common.bits_ops import substring, bit_at
from ..concrete.conditional_add_imm import ConditionalAddImm
from ..concrete.conditional_add_new_imm import ConditionalAddNewImm
from ..concrete.conditional_add_new_reg import ConditionalAddNewReg
from ..concrete.conditional_add_not_imm import ConditionalAddNotImm
from ..concrete.conditional_add_not_new_imm import ConditionalAddNotNewImm
from ..concrete.conditional_add_not_new_reg import ConditionalAddNotNewReg
from ..concrete.conditional_add_not_reg import ConditionalAddNotReg
from ..concrete.conditional_add_reg import ConditionalAddReg
from ..concrete.conditional_and import ConditionalAnd
from ..concrete.conditional_and_new import ConditionalAndNew
from ..concrete.conditional_and_not import ConditionalAndNot
from ..concrete.conditional_and_not_new import ConditionalAndNotNew
from ..concrete.conditional_aslh import ConditionalAslh
from ..concrete.conditional_aslh_new import ConditionalAslhNew
from ..concrete.conditional_aslh_not import ConditionalAslhNot
from ..concrete.conditional_aslh_not_new import ConditionalAslhNotNew
from ..concrete.conditional_asrh import ConditionalAsrh
from ..concrete.conditional_asrh_new import ConditionalAsrhNew
from ..concrete.conditional_asrh_not import ConditionalAsrhNot
from ..concrete.conditional_asrh_not_new import ConditionalAsrhNotNew
from ..concrete.conditional_combine import ConditionalCombine
from ..concrete.conditional_combine_new import ConditionalCombineNew
from ..concrete.conditional_combine_not import ConditionalCombineNot
from ..concrete.conditional_combine_not_new import ConditionalCombineNotNew
from ..concrete.conditional_or import ConditionalOr
from ..concrete.conditional_or_new import ConditionalOrNew
from ..concrete.conditional_or_not import ConditionalOrNot
from ..concrete.conditional_or_not_new import ConditionalOrNotNew
from ..concrete.conditional_sub import ConditionalSub
from ..concrete.conditional_sub_new import ConditionalSubNew
from ..concrete.conditional_sub_not import ConditionalSubNot
from ..concrete.conditional_sub_not_new import ConditionalSubNotNew
from ..concrete.conditional_sxtb import ConditionalSxtb
from ..concrete.conditional_sxtb_new import ConditionalSxtbNew
from ..concrete.conditional_sxtb_not import ConditionalSxtbNot
from ..concrete.conditional_sxtb_not_new import ConditionalSxtbNotNew
from ..concrete.conditional_sxth import ConditionalSxth
from ..concrete.conditional_sxth_new import ConditionalSxthNew
from ..concrete.conditional_sxth_not import ConditionalSxthNot
from ..concrete.conditional_sxth_not_new import ConditionalSxthNotNew
from ..concrete.conditional_transfer import ConditionalTransfer
from ..concrete.conditional_transfer_new import ConditionalTransferNew
from ..concrete.conditional_transfer_not import ConditionalTransferNot
from ..concrete.conditional_transfer_not_new import ConditionalTransferNotNew
from ..concrete.conditional_xor import ConditionalXor
from ..concrete.conditional_xor_new import ConditionalXorNew
from ..concrete.conditional_xor_not import ConditionalXorNot
from ..concrete.conditional_xor_not_new import ConditionalXorNotNew
from ..concrete.conditional_zxtb import ConditionalZxtb
from ..concrete.conditional_zxtb_new import ConditionalZxtbNew
from ..concrete.conditional_zxtb_not import ConditionalZxtbNot
from ..concrete.conditional_zxtb_not_new import ConditionalZxtbNotNew
from ..concrete.conditional_zxth import ConditionalZxth
from ..concrete.conditional_zxth_new import ConditionalZxthNew
from ..concrete.conditional_zxth_not import ConditionalZxthNot
from ..concrete.conditional_zxth_not_new import ConditionalZxthNotNew
from ..concrete.nop import Nop
from ..concrete.q6_p_cmp_eq_ri import Q6PCmpEqRi
from ..concrete.q6_p_cmp_eq_rr import Q6PCmpEqRr
from ..concrete.q6_p_cmp_gt_ri import Q6PCmpGtRi
from ..concrete.q6_p_cmp_gt_rr import Q6PCmpGtRr
from ..concrete.q6_p_cmp_gtu_ri import Q6PCmpGtuRi
from ..concrete.q6_p_cmp_gtu_rr import Q6PCmpGtuRr
from ..concrete.q6_p_combine_ii import Q6PCombineIi
from ..concrete.q6_p_combine_ii_unsigned import Q6PCombineIiUnsigned
from ..concrete.q6_p_combine_ir import Q6PCombineIr
from ..concrete.q6_p_combine_ri import Q6PCombineRi
from ..concrete.q6_p_combine_rr import Q6PCombineRr
from ..concrete.q6_p_not_cmp_eq_ri import Q6PNotCmpEqRi
from ..concrete.q6_p_not_cmp_eq_rr import Q6PNotCmpEqRr
from ..concrete.q6_p_not_cmp_gt_ri import Q6PNotCmpGtRi
from ..concrete.q6_p_not_cmp_gt_rr import Q6PNotCmpGtRr
from ..concrete.q6_p_not_cmp_gtu_ri import Q6PNotCmpGtuRi
from ..concrete.q6_p_not_cmp_gtu_rr import Q6PNotCmpGtuRr
from ..concrete.q6_p_packhl_rr import Q6PPackhlRr
from ..concrete.q6_r_add_ri import Q6RAddRi
from ..concrete.q6_r_add_rr import Q6RAddRr
from ..concrete.q6_r_add_rr_sat import Q6RAddRrSat
from ..concrete.q6_r_and_ri import Q6RAndRi
from ..concrete.q6_r_and_rnr import Q6RAndRnr
from ..concrete.q6_r_and_rr import Q6RAndRr
from ..concrete.q6_r_aslh_r import Q6RAslhR
from ..concrete.q6_r_asrh_r import Q6RAsrhR
from ..concrete.q6_r_cmp_eq_ri import Q6RCmpEqRi
from ..concrete.q6_r_cmp_eq_rr import Q6RCmpEqRr
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
from ..concrete.q6_r_not_cmp_eq_ri import Q6RNotCmpEqRi
from ..concrete.q6_r_not_cmp_eq_rr import Q6RNotCmpEqRr
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

CONDITIONAL_ASLH_S_DN = {
    0b00: ConditionalAslh,
    0b01: ConditionalAslhNew,
    0b10: ConditionalAslhNot,
    0b11: ConditionalAslhNotNew,
}

CONDITIONAL_ASRH_S_DN = {
    0b00: ConditionalAsrh,
    0b01: ConditionalAsrhNew,
    0b10: ConditionalAsrhNot,
    0b11: ConditionalAsrhNotNew,
}

CONDITIONAL_SXTB_S_DN = {
    0b00: ConditionalSxtb,
    0b01: ConditionalSxtbNew,
    0b10: ConditionalSxtbNot,
    0b11: ConditionalSxtbNotNew,
}

CONDITIONAL_SXTH_S_DN = {
    0b00: ConditionalSxth,
    0b01: ConditionalSxthNew,
    0b10: ConditionalSxthNot,
    0b11: ConditionalSxthNotNew,
}

CONDITIONAL_ZXTB_S_DN = {
    0b00: ConditionalZxtb,
    0b01: ConditionalZxtbNew,
    0b10: ConditionalZxtbNot,
    0b11: ConditionalZxtbNotNew,
}

CONDITIONAL_ZXTH_S_DN = {
    0b00: ConditionalZxth,
    0b01: ConditionalZxthNew,
    0b10: ConditionalZxthNot,
    0b11: ConditionalZxthNotNew,
}

CONDITIONAL_TRANSFER_S_DN = {
    (0b0, 0b0): ConditionalTransfer,
    (0b0, 0b1): ConditionalTransferNew,
    (0b1, 0b0): ConditionalTransferNot,
    (0b1, 0b1): ConditionalTransferNotNew,
}

CONDITIONAL_ADD_IMM_S_DN = {
    (0b0, 0b0): ConditionalAddImm,
    (0b0, 0b1): ConditionalAddNewImm,
    (0b1, 0b0): ConditionalAddNotImm,
    (0b1, 0b1): ConditionalAddNotNewImm,
}

CONDITIONAL_ADD_REG_DN_S = {
    (0b0, 0b0): ConditionalAddReg,
    (0b0, 0b1): ConditionalAddNotReg,
    (0b1, 0b0): ConditionalAddNewReg,
    (0b1, 0b1): ConditionalAddNotNewReg,
}

CONDITIONAL_COMBINE_DN_S = {
    (0b0, 0b0): ConditionalCombine,
    (0b0, 0b1): ConditionalCombineNot,
    (0b1, 0b0): ConditionalCombineNew,
    (0b1, 0b1): ConditionalCombineNotNew,
}

CONDITIONAL_AND_DN_S = {
    (0b0, 0b0): ConditionalAnd,
    (0b0, 0b1): ConditionalAndNot,
    (0b1, 0b0): ConditionalAndNew,
    (0b1, 0b1): ConditionalAndNotNew,
}

CONDITIONAL_OR_DN_S = {
    (0b0, 0b0): ConditionalOr,
    (0b0, 0b1): ConditionalOrNot,
    (0b1, 0b0): ConditionalOrNew,
    (0b1, 0b1): ConditionalOrNotNew,
}

CONDITIONAL_XOR_DN_S = {
    (0b0, 0b0): ConditionalXor,
    (0b0, 0b1): ConditionalXorNot,
    (0b1, 0b0): ConditionalXorNew,
    (0b1, 0b1): ConditionalXorNotNew,
}

CONDITIONAL_SUB_DN_S = {
    (0b0, 0b0): ConditionalSub,
    (0b0, 0b1): ConditionalSubNot,
    (0b1, 0b0): ConditionalSubNew,
    (0b1, 0b1): ConditionalSubNotNew,
}


def decode_alu_32_class_7(instruction):
    maj_op = substring(instruction, 26, 24)
    min_op = substring(instruction, 23, 21)
    rs = bit_at(instruction, 27)
    bit_13 = bit_at(instruction, 13)
    if not rs and maj_op == 0b110 and ((min_op >> 1) == 0b00):
        return Q6RAndRi
    if not rs and maj_op == 0b110 and ((min_op >> 1) == 0b10):
        return Q6ROrRi
    if maj_op == 0b111 and rs:
        return Nop
    if maj_op == 0b110 and ((min_op >> 1) == 0b01):
        return Q6RSubIr
    if maj_op == 0b000 and min_op == 0b101 and not bit_13:
        return Q6RSxtbR
    if maj_op == 0b000 and min_op == 0b111 and not bit_13:
        return Q6RSxthR
    if maj_op == 0b000 and rs:
        return Q6REqualsI
    if not rs and maj_op == 0b010 and min_op & 1 == 1:
        return Q6RhEqualsI
    if not rs and maj_op == 0b001 and min_op & 1 == 1:
        return Q6RlEqualsI
    if not rs and maj_op == 0b000 and min_op == 0b011:
        return Q6REqualsR
    if not rs and maj_op == 0b000 and min_op == 0b110 and not bit_13:
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
    if not rs and maj_op == 0b100:
        return CONDITIONAL_ADD_IMM_S_DN[(min_op >> 2), bit_13]
    if not rs and maj_op == 0b000 and min_op == 0b000 and bit_13:
        return CONDITIONAL_ASLH_S_DN[substring(instruction, 11, 10)]
    if not rs and maj_op == 0b000 and min_op == 0b001 and bit_13:
        return CONDITIONAL_ASRH_S_DN[substring(instruction, 11, 10)]
    if not rs and maj_op == 0b000 and min_op == 0b101 and bit_13:
        return CONDITIONAL_SXTB_S_DN[substring(instruction, 11, 10)]
    if not rs and maj_op == 0b000 and min_op == 0b111 and bit_13:
        return CONDITIONAL_SXTH_S_DN[substring(instruction, 11, 10)]
    if rs and maj_op == 0b110:
        return CONDITIONAL_TRANSFER_S_DN[(min_op >> 2), bit_13]
    if not rs and maj_op == 0b000 and min_op == 0b100 and bit_13:
        return CONDITIONAL_ZXTB_S_DN[substring(instruction, 11, 10)]
    if not rs and maj_op == 0b000 and min_op == 0b110 and bit_13:
        return CONDITIONAL_ZXTH_S_DN[substring(instruction, 11, 10)]
    if not rs and maj_op == 0b101 and ((min_op >> 1) == 0b00) and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpEqRi
    if not rs and maj_op == 0b101 and ((min_op >> 1) == 0b00) and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpEqRi
    if not rs and maj_op == 0b101 and ((min_op >> 1) == 0b01) and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpGtRi
    if not rs and maj_op == 0b101 and ((min_op >> 1) == 0b01) and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpGtRi
    if not rs and maj_op == 0b101 and min_op == 0b100 and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpGtuRi
    if not rs and maj_op == 0b101 and min_op == 0b100 and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpGtuRi
    if not rs and maj_op == 0b011 and ((min_op & 0b11) == 0b10) and bit_13:
        return Q6RCmpEqRi
    if not rs and maj_op == 0b011 and ((min_op & 0b11) == 0b11) and bit_13:
        return Q6RNotCmpEqRi


def decode_alu_32_class_15(instruction):
    maj_op = substring(instruction, 26, 24)
    min_op = substring(instruction, 23, 21)
    p = bit_at(instruction, 27)
    bit_13 = bit_at(instruction, 13)
    if not p and maj_op == 0b011 and min_op == 0b000:
        return Q6RAddRr
    if not p and maj_op == 0b110 and min_op == 0b010:
        return Q6RAddRrSat
    if not p and maj_op == 0b001 and min_op == 0b000:
        return Q6RAndRr
    if not p and maj_op == 0b001 and min_op == 0b001:
        return Q6ROrRr
    if not p and maj_op == 0b001 and min_op == 0b011:
        return Q6RXorRr
    if not p and maj_op == 0b001 and min_op == 0b100:
        return Q6RAndRnr
    if not p and maj_op == 0b001 and min_op == 0b101:
        return Q6ROrRnr
    if not p and maj_op == 0b011 and min_op == 0b001:
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
    if not p and maj_op == 0b011 and min_op == 0b100:
        return Q6RCombineRhrh
    if not p and maj_op == 0b011 and min_op == 0b101:
        return Q6RCombineRhrl
    if not p and maj_op == 0b011 and min_op == 0b110:
        return Q6RCombineRlrh
    if not p and maj_op == 0b011 and min_op == 0b111:
        return Q6RCombineRlrl
    if not p and maj_op == 0b101 and ((min_op >> 2) == 0b0):
        return Q6PCombineRr
    if maj_op == 0b100:
        return Q6RMuxPrr
    if maj_op == 0b101 and ((min_op >> 2) == 0b1):
        return Q6PPackhlRr
    if p and maj_op == 0b011 and min_op == 0b000:
        return CONDITIONAL_ADD_REG_DN_S[bit_13, bit_at(instruction, 7)]
    if p and maj_op == 0b101 and min_op == 0b000:
        return CONDITIONAL_COMBINE_DN_S[bit_13, bit_at(instruction, 7)]
    if p and maj_op == 0b001 and ((min_op & 0b11) == 0b00):
        return CONDITIONAL_AND_DN_S[bit_13, bit_at(instruction, 7)]
    if p and maj_op == 0b001 and ((min_op & 0b11) == 0b01):
        return CONDITIONAL_OR_DN_S[bit_13, bit_at(instruction, 7)]
    if p and maj_op == 0b001 and ((min_op & 0b11) == 0b11):
        return CONDITIONAL_XOR_DN_S[bit_13, bit_at(instruction, 7)]
    if p and maj_op == 0b011 and ((min_op & 0b101) == 0b001):
        return CONDITIONAL_SUB_DN_S[bit_13, bit_at(instruction, 7)]
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b00) and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpEqRr
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b00) and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpEqRr
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b10) and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpGtRr
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b10) and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpGtRr
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b11) and substring(instruction, 4, 2) == 0b000:
        return Q6PCmpGtuRr
    if not p and maj_op == 0b010 and ((min_op & 0b11) == 0b11) and substring(instruction, 4, 2) == 0b100:
        return Q6PNotCmpGtuRr
    if not p and maj_op == 0b011 and min_op == 0b010:
        return Q6RCmpEqRr
    if not p and maj_op == 0b011 and min_op == 0b011:
        return Q6RNotCmpEqRr


def decode_alu_32_class(instruction):
    iclass = substring(instruction, 31, 28)
    if iclass == 0b0111:
        return decode_alu_32_class_7(instruction)
    elif iclass == 0b1011:
        return Q6RAddRi
    elif iclass == 0b1111:
        return decode_alu_32_class_15(instruction)
