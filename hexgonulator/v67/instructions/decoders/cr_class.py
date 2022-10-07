from hexgonulator.common.bits_ops import substring, bit_at
from hexgonulator.v67.instructions.concrete.q6_p_all8_p import Q6PAll8P
from hexgonulator.v67.instructions.concrete.q6_p_any8_p import Q6PAny8P
from hexgonulator.v67.instructions.concrete.q6_p_fastcorner9_pp import Q6PFastcorner9Pp
from hexgonulator.v67.instructions.concrete.q6_p_not_fastcorner9_pp import Q6PNotFastcorner9Pp


def decode_cr_class(instruction):
    bits_27_20 = substring(instruction, 27, 20)
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
