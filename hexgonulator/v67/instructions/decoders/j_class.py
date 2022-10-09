from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.call import Call
from hexgonulator.v67.instructions.concrete.callr import Callr
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_imm import CmpEqAndJumpP0Imm
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_imm_hint import CmpEqAndJumpP0ImmHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_imm_not import CmpEqAndJumpP0ImmNot
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_imm_not_hint import CmpEqAndJumpP0ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_minus1 import CmpEqAndJumpP0Minus1
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_minus1_hint import CmpEqAndJumpP0Minus1Hint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_minus1_not import CmpEqAndJumpP0Minus1Not
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_minus1_not_hint import CmpEqAndJumpP0Minus1NotHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_reg import CmpEqAndJumpP0Reg
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_reg_hint import CmpEqAndJumpP0RegHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_reg_not import CmpEqAndJumpP0RegNot
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p0_reg_not_hint import CmpEqAndJumpP0RegNotHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_imm import CmpEqAndJumpP1Imm
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_imm_hint import CmpEqAndJumpP1ImmHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_imm_not import CmpEqAndJumpP1ImmNot
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_imm_not_hint import CmpEqAndJumpP1ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_minus1 import CmpEqAndJumpP1Minus1
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_minus1_hint import CmpEqAndJumpP1Minus1Hint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_minus1_not import CmpEqAndJumpP1Minus1Not
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_minus1_not_hint import CmpEqAndJumpP1Minus1NotHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_reg import CmpEqAndJumpP1Reg
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_reg_hint import CmpEqAndJumpP1RegHint
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_reg_not import CmpEqAndJumpP1RegNot
from hexgonulator.v67.instructions.concrete.cmp_eq_and_jump_p1_reg_not_hint import CmpEqAndJumpP1RegNotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_imm import CmpGtAndJumpP0Imm
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_imm_hint import CmpGtAndJumpP0ImmHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_imm_not import CmpGtAndJumpP0ImmNot
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_imm_not_hint import CmpGtAndJumpP0ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_minus1 import CmpGtAndJumpP0Minus1
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_minus1_hint import CmpGtAndJumpP0Minus1Hint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_minus1_not import CmpGtAndJumpP0Minus1Not
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_minus1_not_hint import CmpGtAndJumpP0Minus1NotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_reg import CmpGtAndJumpP0Reg
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_reg_hint import CmpGtAndJumpP0RegHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_reg_not import CmpGtAndJumpP0RegNot
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p0_reg_not_hint import CmpGtAndJumpP0RegNotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_imm import CmpGtAndJumpP1Imm
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_imm_hint import CmpGtAndJumpP1ImmHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_imm_not import CmpGtAndJumpP1ImmNot
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_imm_not_hint import CmpGtAndJumpP1ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_minus1 import CmpGtAndJumpP1Minus1
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_minus1_hint import CmpGtAndJumpP1Minus1Hint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_minus1_not import CmpGtAndJumpP1Minus1Not
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_minus1_not_hint import CmpGtAndJumpP1Minus1NotHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_reg import CmpGtAndJumpP1Reg
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_reg_hint import CmpGtAndJumpP1RegHint
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_reg_not import CmpGtAndJumpP1RegNot
from hexgonulator.v67.instructions.concrete.cmp_gt_and_jump_p1_reg_not_hint import CmpGtAndJumpP1RegNotHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_imm import CmpGtuAndJumpP0Imm
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_imm_hint import CmpGtuAndJumpP0ImmHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_imm_not import CmpGtuAndJumpP0ImmNot
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_imm_not_hint import CmpGtuAndJumpP0ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_reg import CmpGtuAndJumpP0Reg
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_reg_hint import CmpGtuAndJumpP0RegHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_reg_not import CmpGtuAndJumpP0RegNot
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p0_reg_not_hint import CmpGtuAndJumpP0RegNotHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_imm import CmpGtuAndJumpP1Imm
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_imm_hint import CmpGtuAndJumpP1ImmHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_imm_not import CmpGtuAndJumpP1ImmNot
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_imm_not_hint import CmpGtuAndJumpP1ImmNotHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_reg import CmpGtuAndJumpP1Reg
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_reg_hint import CmpGtuAndJumpP1RegHint
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_reg_not import CmpGtuAndJumpP1RegNot
from hexgonulator.v67.instructions.concrete.cmp_gtu_and_jump_p1_reg_not_hint import CmpGtuAndJumpP1RegNotHint
from hexgonulator.v67.instructions.concrete.conditional_call import ConditionalCall
from hexgonulator.v67.instructions.concrete.conditional_call_not import ConditionalCallNot
from hexgonulator.v67.instructions.concrete.conditional_callr import ConditionalCallr
from hexgonulator.v67.instructions.concrete.conditional_callr_not import ConditionalCallrNot
from hexgonulator.v67.instructions.concrete.conditional_jump import ConditionalJump
from hexgonulator.v67.instructions.concrete.conditional_jump_hint import ConditionalJumpHint
from hexgonulator.v67.instructions.concrete.conditional_jump_new import ConditionalJumpNew
from hexgonulator.v67.instructions.concrete.conditional_jump_new_hint import ConditionalJumpNewHint
from hexgonulator.v67.instructions.concrete.conditional_jump_not import ConditionalJumpNot
from hexgonulator.v67.instructions.concrete.conditional_jump_not_hint import ConditionalJumpNotHint
from hexgonulator.v67.instructions.concrete.conditional_jump_not_new import ConditionalJumpNotNew
from hexgonulator.v67.instructions.concrete.conditional_jump_not_new_hint import ConditionalJumpNotNewHint
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_eq_zero import ConditionalJumpRegEqZero
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_eq_zero_hint import ConditionalJumpRegEqZeroHint
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_gt_zero import ConditionalJumpRegGtZero
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_gt_zero_hint import ConditionalJumpRegGtZeroHint
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_lt_zero import ConditionalJumpRegLtZero
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_lt_zero_hint import ConditionalJumpRegLtZeroHint
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_not_zero import ConditionalJumpRegNotZero
from hexgonulator.v67.instructions.concrete.conditional_jump_reg_not_zero_hint import ConditionalJumpRegNotZeroHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr import ConditionalJumpr
from hexgonulator.v67.instructions.concrete.conditional_jumpr_hint import ConditionalJumprHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_new import ConditionalJumprNew
from hexgonulator.v67.instructions.concrete.conditional_jumpr_new_hint import ConditionalJumprNewHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not import ConditionalJumprNot
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_hint import ConditionalJumprNotHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_new import ConditionalJumprNotNew
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_new_hint import ConditionalJumprNotNewHint
from hexgonulator.v67.instructions.concrete.hintjr import Hintjr
from hexgonulator.v67.instructions.concrete.jump import Jump
from hexgonulator.v67.instructions.concrete.jumpr import Jumpr
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p0 import TstbitAndJumpP0
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p0_hint import TstbitAndJumpP0Hint
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p0_not import TstbitAndJumpP0Not
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p0_not_hint import TstbitAndJumpP0NotHint
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p1 import TstbitAndJumpP1
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p1_hint import TstbitAndJumpP1Hint
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p1_not import TstbitAndJumpP1Not
from hexgonulator.v67.instructions.concrete.tstbit_and_jump_p1_not_hint import TstbitAndJumpP1NotHint

DECODING_27_21 = {
    0b0000101: Callr,
    0b0001000: ConditionalCallr,
    0b0001001: ConditionalCallrNot,
    0b0010101: Hintjr,
    0b0010100: Jumpr,
}

CONDITIONAL_JUMPR_12_11 = {
    0b00: ConditionalJumpr,
    0b01: ConditionalJumprNew,
    0b10: ConditionalJumprHint,
    0b11: ConditionalJumprNewHint,
}

CONDITIONAL_JUMPR_NOT_12_11 = {
    0b00: ConditionalJumprNot,
    0b01: ConditionalJumprNotNew,
    0b10: ConditionalJumprNotHint,
    0b11: ConditionalJumprNotNewHint,
}

CMP_MINUS1_P_NOT_HINT_OP = {
    (0b0, 0b0, 0b0, 0b00): CmpEqAndJumpP0Minus1,
    (0b0, 0b0, 0b0, 0b01): CmpGtAndJumpP0Minus1,
    (0b0, 0b0, 0b0, 0b11): TstbitAndJumpP0,
    (0b0, 0b0, 0b1, 0b00): CmpEqAndJumpP0Minus1Hint,
    (0b0, 0b0, 0b1, 0b01): CmpGtAndJumpP0Minus1Hint,
    (0b0, 0b0, 0b1, 0b11): TstbitAndJumpP0Hint,
    (0b0, 0b1, 0b0, 0b00): CmpEqAndJumpP0Minus1Not,
    (0b0, 0b1, 0b0, 0b01): CmpGtAndJumpP0Minus1Not,
    (0b0, 0b1, 0b0, 0b11): TstbitAndJumpP0Not,
    (0b0, 0b1, 0b1, 0b00): CmpEqAndJumpP0Minus1NotHint,
    (0b0, 0b1, 0b1, 0b01): CmpGtAndJumpP0Minus1NotHint,
    (0b0, 0b1, 0b1, 0b11): TstbitAndJumpP0NotHint,
    (0b1, 0b0, 0b0, 0b00): CmpEqAndJumpP1Minus1,
    (0b1, 0b0, 0b0, 0b01): CmpGtAndJumpP1Minus1,
    (0b1, 0b0, 0b0, 0b11): TstbitAndJumpP1,
    (0b1, 0b0, 0b1, 0b00): CmpEqAndJumpP1Minus1Hint,
    (0b1, 0b0, 0b1, 0b01): CmpGtAndJumpP1Minus1Hint,
    (0b1, 0b0, 0b1, 0b11): TstbitAndJumpP1Hint,
    (0b1, 0b1, 0b0, 0b00): CmpEqAndJumpP1Minus1Not,
    (0b1, 0b1, 0b0, 0b01): CmpGtAndJumpP1Minus1Not,
    (0b1, 0b1, 0b0, 0b11): TstbitAndJumpP1Not,
    (0b1, 0b1, 0b1, 0b00): CmpEqAndJumpP1Minus1NotHint,
    (0b1, 0b1, 0b1, 0b01): CmpGtAndJumpP1Minus1NotHint,
    (0b1, 0b1, 0b1, 0b11): TstbitAndJumpP1NotHint,
}

CMP_IMM_P_OP_NOT_HINT = {
    (0b0, 0b00, 0b0, 0b0): CmpEqAndJumpP0Imm,
    (0b0, 0b00, 0b0, 0b1): CmpEqAndJumpP0ImmHint,
    (0b0, 0b00, 0b1, 0b0): CmpEqAndJumpP0ImmNot,
    (0b0, 0b00, 0b1, 0b1): CmpEqAndJumpP0ImmNotHint,
    (0b0, 0b01, 0b0, 0b0): CmpGtAndJumpP0Imm,
    (0b0, 0b01, 0b0, 0b1): CmpGtAndJumpP0ImmHint,
    (0b0, 0b01, 0b1, 0b0): CmpGtAndJumpP0ImmNot,
    (0b0, 0b01, 0b1, 0b1): CmpGtAndJumpP0ImmNotHint,
    (0b0, 0b10, 0b0, 0b0): CmpGtuAndJumpP0Imm,
    (0b0, 0b10, 0b0, 0b1): CmpGtuAndJumpP0ImmHint,
    (0b0, 0b10, 0b1, 0b0): CmpGtuAndJumpP0ImmNot,
    (0b0, 0b10, 0b1, 0b1): CmpGtuAndJumpP0ImmNotHint,
    (0b1, 0b00, 0b0, 0b0): CmpEqAndJumpP1Imm,
    (0b1, 0b00, 0b0, 0b1): CmpEqAndJumpP1ImmHint,
    (0b1, 0b00, 0b1, 0b0): CmpEqAndJumpP1ImmNot,
    (0b1, 0b00, 0b1, 0b1): CmpEqAndJumpP1ImmNotHint,
    (0b1, 0b01, 0b0, 0b0): CmpGtAndJumpP1Imm,
    (0b1, 0b01, 0b0, 0b1): CmpGtAndJumpP1ImmHint,
    (0b1, 0b01, 0b1, 0b0): CmpGtAndJumpP1ImmNot,
    (0b1, 0b01, 0b1, 0b1): CmpGtAndJumpP1ImmNotHint,
    (0b1, 0b10, 0b0, 0b0): CmpGtuAndJumpP1Imm,
    (0b1, 0b10, 0b0, 0b1): CmpGtuAndJumpP1ImmHint,
    (0b1, 0b10, 0b1, 0b0): CmpGtuAndJumpP1ImmNot,
    (0b1, 0b10, 0b1, 0b1): CmpGtuAndJumpP1ImmNotHint,
}

CMP_REG_OP_NOT_HINT_P = {
    (0b00, 0b0, 0b0, 0b0): CmpEqAndJumpP0Reg,
    (0b00, 0b0, 0b0, 0b1): CmpEqAndJumpP1Reg,
    (0b00, 0b0, 0b1, 0b0): CmpEqAndJumpP0RegHint,
    (0b00, 0b0, 0b1, 0b1): CmpEqAndJumpP1RegHint,
    (0b00, 0b1, 0b0, 0b0): CmpEqAndJumpP0RegNot,
    (0b00, 0b1, 0b0, 0b1): CmpEqAndJumpP1RegNot,
    (0b00, 0b1, 0b1, 0b0): CmpEqAndJumpP0RegNotHint,
    (0b00, 0b1, 0b1, 0b1): CmpEqAndJumpP1RegNotHint,
    (0b01, 0b0, 0b0, 0b0): CmpGtAndJumpP0Reg,
    (0b01, 0b0, 0b0, 0b1): CmpGtAndJumpP1Reg,
    (0b01, 0b0, 0b1, 0b0): CmpGtAndJumpP0RegHint,
    (0b01, 0b0, 0b1, 0b1): CmpGtAndJumpP1RegHint,
    (0b01, 0b1, 0b0, 0b0): CmpGtAndJumpP0RegNot,
    (0b01, 0b1, 0b0, 0b1): CmpGtAndJumpP1RegNot,
    (0b01, 0b1, 0b1, 0b0): CmpGtAndJumpP0RegNotHint,
    (0b01, 0b1, 0b1, 0b1): CmpGtAndJumpP1RegNotHint,
    (0b10, 0b0, 0b0, 0b0): CmpGtuAndJumpP0Reg,
    (0b10, 0b0, 0b0, 0b1): CmpGtuAndJumpP1Reg,
    (0b10, 0b0, 0b1, 0b0): CmpGtuAndJumpP0RegHint,
    (0b10, 0b0, 0b1, 0b1): CmpGtuAndJumpP1RegHint,
    (0b10, 0b1, 0b0, 0b0): CmpGtuAndJumpP0RegNot,
    (0b10, 0b1, 0b0, 0b1): CmpGtuAndJumpP1RegNot,
    (0b10, 0b1, 0b1, 0b0): CmpGtuAndJumpP0RegNotHint,
    (0b10, 0b1, 0b1, 0b1): CmpGtuAndJumpP1RegNotHint,
}

CONDITIONAL_JUMP_NOT_HINT_NEW = {
    (0b0, 0b0, 0b0): ConditionalJump,
    (0b0, 0b1, 0b0): ConditionalJumpHint,
    (0b1, 0b0, 0b0): ConditionalJumpNot,
    (0b1, 0b1, 0b0): ConditionalJumpNotHint,
    (0b0, 0b0, 0b1): ConditionalJumpNew,
    (0b0, 0b1, 0b1): ConditionalJumpNewHint,
    (0b1, 0b0, 0b1): ConditionalJumpNotNew,
    (0b1, 0b1, 0b1): ConditionalJumpNotNewHint,
}

CONDITIONAL_JUMP_REG_OP_HINT = {
    (0b00, 0b0): ConditionalJumpRegNotZero,
    (0b00, 0b1): ConditionalJumpRegNotZeroHint,
    (0b01, 0b0): ConditionalJumpRegGtZero,
    (0b01, 0b1): ConditionalJumpRegGtZeroHint,
    (0b10, 0b0): ConditionalJumpRegEqZero,
    (0b10, 0b1): ConditionalJumpRegEqZeroHint,
    (0b11, 0b0): ConditionalJumpRegLtZero,
    (0b11, 0b1): ConditionalJumpRegLtZeroHint,
}


def decode_jr_class(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b0011010:
        bit_12_11 = substring(instruction, 12, 11)
        return CONDITIONAL_JUMPR_12_11[bit_12_11]
    if bits_27_21 == 0b0011011:
        bit_12_11 = substring(instruction, 12, 11)
        return CONDITIONAL_JUMPR_NOT_12_11[bit_12_11]
    return DECODING_27_21.get(bits_27_21)


def decode_j_jr_class(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    bits_27_24 = substring(instruction, 27, 24)
    bit_21 = bit_at(instruction, 21)
    if bits_27_21 in (0b0011010, 0b0011011, 0b0000101, 0b0001000, 0b0001001, 0b0010101, 0b0010100):
        return decode_jr_class(instruction)
    if substring(instruction, 27, 25) == 0b101:
        return Call
    if bits_27_24 == 0b1101 and not bit_21:
        return ConditionalCall
    if bits_27_24 == 0b1101 and bit_21:
        return ConditionalCallNot
    if substring(instruction, 27, 25) == 0b100:
        return Jump
    if bits_27_24 == 0b1100:
        return CONDITIONAL_JUMP_NOT_HINT_NEW[bit_21, bit_at(instruction, 12), bit_at(instruction, 11)]


def decode_j_class_1(instruction):
    bits_27_26 = substring(instruction, 27, 26)
    bits_24_23 = substring(instruction, 24, 23)
    bits_9_8 = substring(instruction, 9, 8)
    bit_13 = bit_at(instruction, 13)
    bit_22 = bit_at(instruction, 22)
    if bits_27_26 == 0b00 and bits_24_23 == 0b11:
        return CMP_MINUS1_P_NOT_HINT_OP[bit_at(instruction, 25), bit_22, bit_13, bits_9_8]
    if bits_27_26 == 0b00 and bits_24_23 != 0b11:
        return CMP_IMM_P_OP_NOT_HINT[bit_at(instruction, 25), bits_24_23, bit_22, bit_13]
    if substring(instruction, 27, 25) == 0b010 and bits_24_23 != 0b11:
        return CMP_REG_OP_NOT_HINT_P[bits_24_23, bit_22, bit_13, bit_at(instruction, 12)]


def decode_j_class_6(instruction):
    bits_27_24 = substring(instruction, 27, 24)
    if bits_27_24 == 0b0001:
        return CONDITIONAL_JUMP_REG_OP_HINT[substring(instruction, 23, 22), bit_at(instruction, 12)]
