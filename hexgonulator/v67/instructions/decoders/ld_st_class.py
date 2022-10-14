from hexgonulator.common.bits_ops import substring, bit_at
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


def decode_class_3(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b1010110:
        return ReadDRegRegOff


def decode_class_4(instruction):
    if bit_at(instruction, 27) == 0b1 and substring(instruction, 24, 21) == 0b1110:
        return ReadDGpImm


def decode_class_9(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    bit_12 = bit_at(instruction, 12)
    if bit_at(instruction, 27) == 0b0 and substring(instruction, 24, 21) == 0b1110:
        return ReadDRegImm
    if bits_27_21 == 0b1001110 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b0:
        return Q6RMemdImCirc
    if bits_27_21 == 0b1001110 and bit_12 == 0b0 and bit_at(instruction, 9) == 0b1 and bit_at(instruction, 7) == 0b0:
        return Q6RMemdMCirc
    if bits_27_21 == 0b1011110 and substring(instruction, 13, 12) == 0b01:
        return ReadDSetImm
    if bits_27_21 == 0b1011110 and substring(instruction, 13, 12) == 0b00:
        return ReadDIncImm
    if bits_27_21 == 0b1101110 and bit_12 == 0b1:
        return ReadDImmRegOff
    if bits_27_21 == 0b1101110 and bit_12 == 0b0 and bit_at(instruction, 7) == 0b0:
        return ReadDIncReg
    if bits_27_21 == 0b1111110 and bit_12 == 0b0 and bit_at(instruction, 7) == 0b0:
        return ReadDIncRegBrev
