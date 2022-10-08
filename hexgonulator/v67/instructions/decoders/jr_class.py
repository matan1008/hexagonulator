from hexgonulator.common.bits_ops import substring
from hexgonulator.v67.instructions.concrete.callr import Callr
from hexgonulator.v67.instructions.concrete.conditional_callr import ConditionalCallr
from hexgonulator.v67.instructions.concrete.conditional_callr_not import ConditionalCallrNot
from hexgonulator.v67.instructions.concrete.hintjr import Hintjr


def decode_jr_class(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b0000101:
        return Callr
    if bits_27_21 == 0b0001000:
        return ConditionalCallr
    if bits_27_21 == 0b0001001:
        return ConditionalCallrNot
    if bits_27_21 == 0b0010101:
        return Hintjr
