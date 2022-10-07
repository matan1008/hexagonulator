from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.add_to_pc import AddToPc
from hexgonulator.v67.instructions.concrete.loop0_imm import Loop0Imm
from hexgonulator.v67.instructions.concrete.loop0_reg import Loop0Reg
from hexgonulator.v67.instructions.concrete.loop1_imm import Loop1Imm
from hexgonulator.v67.instructions.concrete.loop1_reg import Loop1Reg
from hexgonulator.v67.instructions.concrete.q6_p_all8_p import Q6PAll8P
from hexgonulator.v67.instructions.concrete.q6_p_any8_p import Q6PAny8P
from hexgonulator.v67.instructions.concrete.q6_p_fastcorner9_pp import Q6PFastcorner9Pp
from hexgonulator.v67.instructions.concrete.q6_p_not_fastcorner9_pp import Q6PNotFastcorner9Pp


def decode_cr_class(instruction):
    bits_27_20 = substring(instruction, 27, 20)
    bits_27_21 = substring(instruction, 27, 21)
    bit_13 = bit_at(instruction, 13)
    bit_7 = bit_at(instruction, 7)
    bit_4 = bit_at(instruction, 4)
    if bits_27_20 == 0b10110000 and bit_13 and bit_7 and bit_4:
        return Q6PFastcorner9Pp
    if bits_27_20 == 0b10110001 and bit_13 and bit_7 and bit_4:
        return Q6PNotFastcorner9Pp
    if bits_27_20 == 0b10111000 and not bit_13:
        return Q6PAny8P
    if bits_27_20 == 0b10111010 and not bit_13:
        return Q6PAll8P
    if bits_27_21 == 0b0000000:
        return Loop0Reg
    if bits_27_21 == 0b0000001:
        return Loop1Reg
    if bits_27_21 == 0b1001000:
        return Loop0Imm
    if bits_27_21 == 0b1001001:
        return Loop1Imm
    if substring(instruction, 27, 16) == 0b101001001001:
        return AddToPc
