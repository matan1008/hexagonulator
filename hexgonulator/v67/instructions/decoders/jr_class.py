from hexgonulator.common.bits_ops import substring
from hexgonulator.v67.instructions.concrete.callr import Callr
from hexgonulator.v67.instructions.concrete.conditional_callr import ConditionalCallr
from hexgonulator.v67.instructions.concrete.conditional_callr_not import ConditionalCallrNot
from hexgonulator.v67.instructions.concrete.conditional_jumpr import ConditionalJumpr
from hexgonulator.v67.instructions.concrete.conditional_jumpr_hint import ConditionalJumprHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_new import ConditionalJumprNew
from hexgonulator.v67.instructions.concrete.conditional_jumpr_new_hint import ConditionalJumprNewHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not import ConditionalJumprNot
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_hint import ConditionalJumprNotHint
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_new import ConditionalJumprNotNew
from hexgonulator.v67.instructions.concrete.conditional_jumpr_not_new_hint import ConditionalJumprNotNewHint
from hexgonulator.v67.instructions.concrete.hintjr import Hintjr
from hexgonulator.v67.instructions.concrete.jumpr import Jumpr

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


def decode_jr_class(instruction):
    bits_27_21 = substring(instruction, 27, 21)
    if bits_27_21 == 0b0011010:
        bit_12_11 = substring(instruction, 12, 11)
        return CONDITIONAL_JUMPR_12_11[bit_12_11]
    if bits_27_21 == 0b0011011:
        bit_12_11 = substring(instruction, 12, 11)
        return CONDITIONAL_JUMPR_NOT_12_11[bit_12_11]
    return DECODING_27_21.get(bits_27_21)
