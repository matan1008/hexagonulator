from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.conditional_read_d_imm import ConditionalReadDImm
from hexgonulator.v67.instructions.concrete.conditional_read_d_imm_new import ConditionalReadDImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_imm_not import ConditionalReadDImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_d_imm_not_new import ConditionalReadDImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_inc_imm import ConditionalReadDIncImm
from hexgonulator.v67.instructions.concrete.conditional_read_d_inc_imm_new import ConditionalReadDIncImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_inc_imm_not import ConditionalReadDIncImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_d_inc_imm_not_new import ConditionalReadDIncImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_imm import ConditionalReadDRegImm
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_imm_new import ConditionalReadDRegImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_imm_not import ConditionalReadDRegImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_imm_not_new import ConditionalReadDRegImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_reg_off import ConditionalReadDRegRegOff
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_reg_off_new import ConditionalReadDRegRegOffNew
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_reg_off_not import ConditionalReadDRegRegOffNot
from hexgonulator.v67.instructions.concrete.conditional_read_d_reg_reg_off_not_new import \
    ConditionalReadDRegRegOffNotNew
from hexgonulator.v67.instructions.concrete.q6_r_memd_im_circ import Q6RMemdImCirc
from hexgonulator.v67.instructions.concrete.q6_r_memd_m_circ import Q6RMemdMCirc
from hexgonulator.v67.instructions.concrete.read_d_gp_imm import ReadDGpImm
from hexgonulator.v67.instructions.concrete.read_d_imm_reg_off import ReadDImmRegOff
from hexgonulator.v67.instructions.concrete.read_d_inc_imm import ReadDIncImm
from hexgonulator.v67.instructions.concrete.read_d_inc_reg import ReadDIncReg
from hexgonulator.v67.instructions.concrete.read_d_inc_reg_brev import ReadDIncRegBrev
from hexgonulator.v67.instructions.concrete.read_d_reg_imm import ReadDRegImm
from hexgonulator.v67.instructions.concrete.read_d_reg_reg_off import ReadDRegRegOff
from hexgonulator.v67.instructions.concrete.read_d_set_imm import ReadDSetImm

CONDITIONAL_READ_D_REG_REG_OFF_NEW_NOT = {
    (0b0, 0b0): ConditionalReadDRegRegOff,
    (0b0, 0b1): ConditionalReadDRegRegOffNot,
    (0b1, 0b0): ConditionalReadDRegRegOffNew,
    (0b1, 0b1): ConditionalReadDRegRegOffNotNew,
}

CONDITIONAL_READ_D_REG_IMM_NOT_NEW = {
    (0b0, 0b0): ConditionalReadDRegImm,
    (0b0, 0b1): ConditionalReadDRegImmNew,
    (0b1, 0b0): ConditionalReadDRegImmNot,
    (0b1, 0b1): ConditionalReadDRegImmNotNew,
}

CONDITIONAL_READ_D_INC_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadDIncImm,
    (0b0, 0b1): ConditionalReadDIncImmNot,
    (0b1, 0b0): ConditionalReadDIncImmNew,
    (0b1, 0b1): ConditionalReadDIncImmNotNew,
}

CONDITIONAL_READ_D_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadDImm,
    (0b0, 0b1): ConditionalReadDImmNot,
    (0b1, 0b0): ConditionalReadDImmNew,
    (0b1, 0b1): ConditionalReadDImmNotNew,
}


def decode_class_3(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b1010110:
        return ReadDRegRegOff
    if substring(instruction, 27, 26) == 0b00 and substring(instruction, 23, 21) == 0b110:
        return CONDITIONAL_READ_D_REG_REG_OFF_NEW_NOT[bit_at(instruction, 25), bit_at(instruction, 24)]


def decode_class_4(instruction):
    bit_27 = bit_at(instruction, 27)
    bits_24_21 = substring(instruction, 24, 21)
    if bit_27 == 0b1 and bits_24_21 == 0b1110:
        return ReadDGpImm
    if bit_27 == 0b0 and bits_24_21 == 0b1110:
        return CONDITIONAL_READ_D_REG_IMM_NOT_NEW[bit_at(instruction, 26), bit_at(instruction, 25)]


def decode_class_9(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    bit_12 = bit_at(instruction, 12)
    bit_7 = bit_at(instruction, 7)
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b1110:
        return ReadDRegImm
    if bits_27_21 == 0b1001110 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return Q6RMemdImCirc
    if bits_27_21 == 0b1001110 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return Q6RMemdMCirc
    if bits_27_21 == 0b1011110 and substring(instruction, 13, 12) == 0b01:
        return ReadDSetImm
    if bits_27_21 == 0b1011110 and substring(instruction, 13, 12) == 0b00:
        return ReadDIncImm
    if bits_27_21 == 0b1101110 and bit_12 == 0b1:
        return ReadDImmRegOff
    if bits_27_21 == 0b1101110 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadDIncReg
    if bits_27_21 == 0b1111110 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadDIncRegBrev
    if bits_27_21 == 0b1011110 and bit_at(instruction, 13):
        return CONDITIONAL_READ_D_INC_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bits_27_21 == 0b1111110 and bit_at(instruction, 13) and bit_7:
        return CONDITIONAL_READ_D_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
