from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.conditional_read_b_imm import ConditionalReadBImm
from hexgonulator.v67.instructions.concrete.conditional_read_b_imm_new import ConditionalReadBImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_imm_not import ConditionalReadBImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_b_imm_not_new import ConditionalReadBImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_inc_imm import ConditionalReadBIncImm
from hexgonulator.v67.instructions.concrete.conditional_read_b_inc_imm_new import ConditionalReadBIncImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_inc_imm_not import ConditionalReadBIncImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_b_inc_imm_not_new import ConditionalReadBIncImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_imm import ConditionalReadBRegImm
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_imm_new import ConditionalReadBRegImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_imm_not import ConditionalReadBRegImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_imm_not_new import ConditionalReadBRegImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_reg_off import ConditionalReadBRegRegOff
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_reg_off_new import ConditionalReadBRegRegOffNew
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_reg_off_not import ConditionalReadBRegRegOffNot
from hexgonulator.v67.instructions.concrete.conditional_read_b_reg_reg_off_not_new import \
    ConditionalReadBRegRegOffNotNew
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
from hexgonulator.v67.instructions.concrete.conditional_read_h_imm import ConditionalReadHImm
from hexgonulator.v67.instructions.concrete.conditional_read_h_imm_new import ConditionalReadHImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_imm_not import ConditionalReadHImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_h_imm_not_new import ConditionalReadHImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_inc_imm import ConditionalReadHIncImm
from hexgonulator.v67.instructions.concrete.conditional_read_h_inc_imm_new import ConditionalReadHIncImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_inc_imm_not import ConditionalReadHIncImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_h_inc_imm_not_new import ConditionalReadHIncImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_imm import ConditionalReadHRegImm
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_imm_new import ConditionalReadHRegImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_imm_not import ConditionalReadHRegImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_imm_not_new import ConditionalReadHRegImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_reg_off import ConditionalReadHRegRegOff
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_reg_off_new import ConditionalReadHRegRegOffNew
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_reg_off_not import ConditionalReadHRegRegOffNot
from hexgonulator.v67.instructions.concrete.conditional_read_h_reg_reg_off_not_new import \
    ConditionalReadHRegRegOffNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_imm import ConditionalReadUbImm
from hexgonulator.v67.instructions.concrete.conditional_read_ub_imm_new import ConditionalReadUbImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_imm_not import ConditionalReadUbImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_ub_imm_not_new import ConditionalReadUbImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_inc_imm import ConditionalReadUbIncImm
from hexgonulator.v67.instructions.concrete.conditional_read_ub_inc_imm_new import ConditionalReadUbIncImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_inc_imm_not import ConditionalReadUbIncImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_ub_inc_imm_not_new import ConditionalReadUbIncImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_imm import ConditionalReadUbRegImm
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_imm_new import ConditionalReadUbRegImmNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_imm_not import ConditionalReadUbRegImmNot
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_imm_not_new import ConditionalReadUbRegImmNotNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_reg_off import ConditionalReadUbRegRegOff
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_reg_off_new import ConditionalReadUbRegRegOffNew
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_reg_off_not import ConditionalReadUbRegRegOffNot
from hexgonulator.v67.instructions.concrete.conditional_read_ub_reg_reg_off_not_new import \
    ConditionalReadUbRegRegOffNotNew
from hexgonulator.v67.instructions.concrete.memb_fifo_im_circ import MembFifoImCirc
from hexgonulator.v67.instructions.concrete.memb_fifo_imm_reg_off import MembFifoImmRegOff
from hexgonulator.v67.instructions.concrete.memb_fifo_inc_imm import MembFifoIncImm
from hexgonulator.v67.instructions.concrete.memb_fifo_inc_reg import MembFifoIncReg
from hexgonulator.v67.instructions.concrete.memb_fifo_inc_reg_brev import MembFifoIncRegBrev
from hexgonulator.v67.instructions.concrete.memb_fifo_m_circ import MembFifoMCirc
from hexgonulator.v67.instructions.concrete.memb_fifo_reg_imm import MembFifoRegImm
from hexgonulator.v67.instructions.concrete.memb_fifo_set_imm import MembFifoSetImm
from hexgonulator.v67.instructions.concrete.memh_fifo_im_circ import MemhFifoImCirc
from hexgonulator.v67.instructions.concrete.memh_fifo_imm_reg_off import MemhFifoImmRegOff
from hexgonulator.v67.instructions.concrete.memh_fifo_inc_imm import MemhFifoIncImm
from hexgonulator.v67.instructions.concrete.memh_fifo_inc_reg import MemhFifoIncReg
from hexgonulator.v67.instructions.concrete.memh_fifo_inc_reg_brev import MemhFifoIncRegBrev
from hexgonulator.v67.instructions.concrete.memh_fifo_m_circ import MemhFifoMCirc
from hexgonulator.v67.instructions.concrete.memh_fifo_reg_imm import MemhFifoRegImm
from hexgonulator.v67.instructions.concrete.memh_fifo_set_imm import MemhFifoSetImm
from hexgonulator.v67.instructions.concrete.q6_r_memb_im_circ import Q6RMembImCirc
from hexgonulator.v67.instructions.concrete.q6_r_memb_m_circ import Q6RMembMCirc
from hexgonulator.v67.instructions.concrete.q6_r_memd_im_circ import Q6RMemdImCirc
from hexgonulator.v67.instructions.concrete.q6_r_memd_m_circ import Q6RMemdMCirc
from hexgonulator.v67.instructions.concrete.q6_r_memh_im_circ import Q6RMemhImCirc
from hexgonulator.v67.instructions.concrete.q6_r_memh_m_circ import Q6RMemhMCirc
from hexgonulator.v67.instructions.concrete.q6_r_memub_im_circ import Q6RMemubImCirc
from hexgonulator.v67.instructions.concrete.q6_r_memub_m_circ import Q6RMemubMCirc
from hexgonulator.v67.instructions.concrete.read_b_gp_imm import ReadBGpImm
from hexgonulator.v67.instructions.concrete.read_b_imm_reg_off import ReadBImmRegOff
from hexgonulator.v67.instructions.concrete.read_b_inc_imm import ReadBIncImm
from hexgonulator.v67.instructions.concrete.read_b_inc_reg import ReadBIncReg
from hexgonulator.v67.instructions.concrete.read_b_inc_reg_brev import ReadBIncRegBrev
from hexgonulator.v67.instructions.concrete.read_b_reg_imm import ReadBRegImm
from hexgonulator.v67.instructions.concrete.read_b_reg_reg_off import ReadBRegRegOff
from hexgonulator.v67.instructions.concrete.read_b_set_imm import ReadBSetImm
from hexgonulator.v67.instructions.concrete.read_d_gp_imm import ReadDGpImm
from hexgonulator.v67.instructions.concrete.read_d_imm_reg_off import ReadDImmRegOff
from hexgonulator.v67.instructions.concrete.read_d_inc_imm import ReadDIncImm
from hexgonulator.v67.instructions.concrete.read_d_inc_reg import ReadDIncReg
from hexgonulator.v67.instructions.concrete.read_d_inc_reg_brev import ReadDIncRegBrev
from hexgonulator.v67.instructions.concrete.read_d_reg_imm import ReadDRegImm
from hexgonulator.v67.instructions.concrete.read_d_reg_reg_off import ReadDRegRegOff
from hexgonulator.v67.instructions.concrete.read_d_set_imm import ReadDSetImm
from hexgonulator.v67.instructions.concrete.read_h_gp_imm import ReadHGpImm
from hexgonulator.v67.instructions.concrete.read_h_imm_reg_off import ReadHImmRegOff
from hexgonulator.v67.instructions.concrete.read_h_inc_imm import ReadHIncImm
from hexgonulator.v67.instructions.concrete.read_h_inc_reg import ReadHIncReg
from hexgonulator.v67.instructions.concrete.read_h_inc_reg_brev import ReadHIncRegBrev
from hexgonulator.v67.instructions.concrete.read_h_reg_imm import ReadHRegImm
from hexgonulator.v67.instructions.concrete.read_h_reg_reg_off import ReadHRegRegOff
from hexgonulator.v67.instructions.concrete.read_h_set_imm import ReadHSetImm
from hexgonulator.v67.instructions.concrete.read_ub_gp_imm import ReadUbGpImm
from hexgonulator.v67.instructions.concrete.read_ub_imm_reg_off import ReadUbImmRegOff
from hexgonulator.v67.instructions.concrete.read_ub_inc_imm import ReadUbIncImm
from hexgonulator.v67.instructions.concrete.read_ub_inc_reg import ReadUbIncReg
from hexgonulator.v67.instructions.concrete.read_ub_inc_reg_brev import ReadUbIncRegBrev
from hexgonulator.v67.instructions.concrete.read_ub_reg_imm import ReadUbRegImm
from hexgonulator.v67.instructions.concrete.read_ub_reg_reg_off import ReadUbRegRegOff
from hexgonulator.v67.instructions.concrete.read_ub_set_imm import ReadUbSetImm

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

CONDITIONAL_READ_B_REG_REG_OFF_NEW_NOT = {
    (0b0, 0b0): ConditionalReadBRegRegOff,
    (0b0, 0b1): ConditionalReadBRegRegOffNot,
    (0b1, 0b0): ConditionalReadBRegRegOffNew,
    (0b1, 0b1): ConditionalReadBRegRegOffNotNew,
}

CONDITIONAL_READ_B_REG_IMM_NOT_NEW = {
    (0b0, 0b0): ConditionalReadBRegImm,
    (0b0, 0b1): ConditionalReadBRegImmNew,
    (0b1, 0b0): ConditionalReadBRegImmNot,
    (0b1, 0b1): ConditionalReadBRegImmNotNew,
}

CONDITIONAL_READ_B_INC_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadBIncImm,
    (0b0, 0b1): ConditionalReadBIncImmNot,
    (0b1, 0b0): ConditionalReadBIncImmNew,
    (0b1, 0b1): ConditionalReadBIncImmNotNew,
}

CONDITIONAL_READ_B_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadBImm,
    (0b0, 0b1): ConditionalReadBImmNot,
    (0b1, 0b0): ConditionalReadBImmNew,
    (0b1, 0b1): ConditionalReadBImmNotNew,
}

CONDITIONAL_READ_H_REG_REG_OFF_NEW_NOT = {
    (0b0, 0b0): ConditionalReadHRegRegOff,
    (0b0, 0b1): ConditionalReadHRegRegOffNot,
    (0b1, 0b0): ConditionalReadHRegRegOffNew,
    (0b1, 0b1): ConditionalReadHRegRegOffNotNew,
}

CONDITIONAL_READ_H_REG_IMM_NOT_NEW = {
    (0b0, 0b0): ConditionalReadHRegImm,
    (0b0, 0b1): ConditionalReadHRegImmNew,
    (0b1, 0b0): ConditionalReadHRegImmNot,
    (0b1, 0b1): ConditionalReadHRegImmNotNew,
}

CONDITIONAL_READ_H_INC_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadHIncImm,
    (0b0, 0b1): ConditionalReadHIncImmNot,
    (0b1, 0b0): ConditionalReadHIncImmNew,
    (0b1, 0b1): ConditionalReadHIncImmNotNew,
}

CONDITIONAL_READ_H_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadHImm,
    (0b0, 0b1): ConditionalReadHImmNot,
    (0b1, 0b0): ConditionalReadHImmNew,
    (0b1, 0b1): ConditionalReadHImmNotNew,
}

CONDITIONAL_READ_UB_REG_REG_OFF_NEW_NOT = {
    (0b0, 0b0): ConditionalReadUbRegRegOff,
    (0b0, 0b1): ConditionalReadUbRegRegOffNot,
    (0b1, 0b0): ConditionalReadUbRegRegOffNew,
    (0b1, 0b1): ConditionalReadUbRegRegOffNotNew,
}

CONDITIONAL_READ_UB_REG_IMM_NOT_NEW = {
    (0b0, 0b0): ConditionalReadUbRegImm,
    (0b0, 0b1): ConditionalReadUbRegImmNew,
    (0b1, 0b0): ConditionalReadUbRegImmNot,
    (0b1, 0b1): ConditionalReadUbRegImmNotNew,
}

CONDITIONAL_READ_UB_INC_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadUbIncImm,
    (0b0, 0b1): ConditionalReadUbIncImmNot,
    (0b1, 0b0): ConditionalReadUbIncImmNew,
    (0b1, 0b1): ConditionalReadUbIncImmNotNew,
}

CONDITIONAL_READ_UB_IMM_NEW_NOT = {
    (0b0, 0b0): ConditionalReadUbImm,
    (0b0, 0b1): ConditionalReadUbImmNot,
    (0b1, 0b0): ConditionalReadUbImmNew,
    (0b1, 0b1): ConditionalReadUbImmNotNew,
}


def decode_class_3(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b1010110:
        return ReadDRegRegOff
    if substring(instruction, 27, 26) == 0b00 and substring(instruction, 23, 21) == 0b110:
        return CONDITIONAL_READ_D_REG_REG_OFF_NEW_NOT[bit_at(instruction, 25), bit_at(instruction, 24)]
    if bits_27_21 == 0b1010000:
        return ReadBRegRegOff
    if substring(instruction, 27, 26) == 0b00 and substring(instruction, 23, 21) == 0b000:
        return CONDITIONAL_READ_B_REG_REG_OFF_NEW_NOT[bit_at(instruction, 25), bit_at(instruction, 24)]
    if bits_27_21 == 0b1010010:
        return ReadHRegRegOff
    if substring(instruction, 27, 26) == 0b00 and substring(instruction, 23, 21) == 0b010:
        return CONDITIONAL_READ_H_REG_REG_OFF_NEW_NOT[bit_at(instruction, 25), bit_at(instruction, 24)]
    if bits_27_21 == 0b1010001:
        return ReadUbRegRegOff
    if substring(instruction, 27, 26) == 0b00 and substring(instruction, 23, 21) == 0b001:
        return CONDITIONAL_READ_UB_REG_REG_OFF_NEW_NOT[bit_at(instruction, 25), bit_at(instruction, 24)]


def decode_class_4(instruction):
    bit_27 = bit_at(instruction, 27)
    bits_24_21 = substring(instruction, 24, 21)
    if bit_27 == 0b1 and bits_24_21 == 0b1110:
        return ReadDGpImm
    if bit_27 == 0b0 and bits_24_21 == 0b1110:
        return CONDITIONAL_READ_D_REG_IMM_NOT_NEW[bit_at(instruction, 26), bit_at(instruction, 25)]
    if bit_27 == 0b1 and bits_24_21 == 0b1000:
        return ReadBGpImm
    if bit_27 == 0b0 and bits_24_21 == 0b1000:
        return CONDITIONAL_READ_B_REG_IMM_NOT_NEW[bit_at(instruction, 26), bit_at(instruction, 25)]
    if bit_27 == 0b1 and bits_24_21 == 0b1010:
        return ReadHGpImm
    if bit_27 == 0b0 and bits_24_21 == 0b1010:
        return CONDITIONAL_READ_H_REG_IMM_NOT_NEW[bit_at(instruction, 26), bit_at(instruction, 25)]
    if bit_27 == 0b1 and bits_24_21 == 0b1001:
        return ReadUbGpImm
    if bit_27 == 0b0 and bits_24_21 == 0b1001:
        return CONDITIONAL_READ_UB_REG_IMM_NOT_NEW[bit_at(instruction, 26), bit_at(instruction, 25)]


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
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b1000:
        return ReadBRegImm
    if bits_27_21 == 0b1001000 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return Q6RMembImCirc
    if bits_27_21 == 0b1001000 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return Q6RMembMCirc
    if bits_27_21 == 0b1011000 and substring(instruction, 13, 12) == 0b01:
        return ReadBSetImm
    if bits_27_21 == 0b1011000 and substring(instruction, 13, 12) == 0b00:
        return ReadBIncImm
    if bits_27_21 == 0b1101000 and bit_12 == 0b1:
        return ReadBImmRegOff
    if bits_27_21 == 0b1101000 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadBIncReg
    if bits_27_21 == 0b1111000 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadBIncRegBrev
    if bits_27_21 == 0b1011000 and bit_at(instruction, 13):
        return CONDITIONAL_READ_B_INC_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bits_27_21 == 0b1111000 and bit_at(instruction, 13) and bit_7:
        return CONDITIONAL_READ_B_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b0100:
        return MembFifoRegImm
    if bits_27_21 == 0b1000100 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return MembFifoImCirc
    if bits_27_21 == 0b1000100 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return MembFifoMCirc
    if bits_27_21 == 0b1010100 and substring(instruction, 13, 12) == 0b01:
        return MembFifoSetImm
    if bits_27_21 == 0b1010100 and substring(instruction, 13, 12) == 0b00:
        return MembFifoIncImm
    if bits_27_21 == 0b1100100 and bit_12 == 0b1:
        return MembFifoImmRegOff
    if bits_27_21 == 0b1100100 and bit_12 == 0b0 and bit_7 == 0b0:
        return MembFifoIncReg
    if bits_27_21 == 0b1110100 and bit_12 == 0b0 and bit_7 == 0b0:
        return MembFifoIncRegBrev
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b0010:
        return MemhFifoRegImm
    if bits_27_21 == 0b1000010 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return MemhFifoImCirc
    if bits_27_21 == 0b1000010 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return MemhFifoMCirc
    if bits_27_21 == 0b1010010 and substring(instruction, 13, 12) == 0b01:
        return MemhFifoSetImm
    if bits_27_21 == 0b1010010 and substring(instruction, 13, 12) == 0b00:
        return MemhFifoIncImm
    if bits_27_21 == 0b1100010 and bit_12 == 0b1:
        return MemhFifoImmRegOff
    if bits_27_21 == 0b1100010 and bit_12 == 0b0 and bit_7 == 0b0:
        return MemhFifoIncReg
    if bits_27_21 == 0b1110010 and bit_12 == 0b0 and bit_7 == 0b0:
        return MemhFifoIncRegBrev
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b1010:
        return ReadHRegImm
    if bits_27_21 == 0b1001010 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return Q6RMemhImCirc
    if bits_27_21 == 0b1001010 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return Q6RMemhMCirc
    if bits_27_21 == 0b1011010 and substring(instruction, 13, 12) == 0b01:
        return ReadHSetImm
    if bits_27_21 == 0b1011010 and substring(instruction, 13, 12) == 0b00:
        return ReadHIncImm
    if bits_27_21 == 0b1101010 and bit_12 == 0b1:
        return ReadHImmRegOff
    if bits_27_21 == 0b1101010 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadHIncReg
    if bits_27_21 == 0b1111010 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadHIncRegBrev
    if bits_27_21 == 0b1011010 and bit_at(instruction, 13):
        return CONDITIONAL_READ_H_INC_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bits_27_21 == 0b1111010 and bit_at(instruction, 13) and bit_7:
        return CONDITIONAL_READ_H_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b1001:
        return ReadUbRegImm
    if bits_27_21 == 0b1001001 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return Q6RMemubImCirc
    if bits_27_21 == 0b1001001 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_7 == 0b0:
        return Q6RMemubMCirc
    if bits_27_21 == 0b1011001 and substring(instruction, 13, 12) == 0b01:
        return ReadUbSetImm
    if bits_27_21 == 0b1011001 and substring(instruction, 13, 12) == 0b00:
        return ReadUbIncImm
    if bits_27_21 == 0b1101001 and bit_12 == 0b1:
        return ReadUbImmRegOff
    if bits_27_21 == 0b1101001 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadUbIncReg
    if bits_27_21 == 0b1111001 and bit_12 == 0b0 and bit_7 == 0b0:
        return ReadUbIncRegBrev
    if bits_27_21 == 0b1011001 and bit_at(instruction, 13):
        return CONDITIONAL_READ_UB_INC_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
    if bits_27_21 == 0b1111001 and bit_at(instruction, 13) and bit_7:
        return CONDITIONAL_READ_UB_IMM_NEW_NOT[bit_12, bit_at(instruction, 11)]
