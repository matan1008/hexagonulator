from hexgonulator.common.bits_ops import substring
from .alu32_class import decode_alu_32_class
from .cr_class import decode_cr_class
from .j_class import decode_j_jr_class
from ..concrete.constant_extender import ConstantExtender

DECODERS = {
    0b0000: lambda instruction: ConstantExtender,
    0b0101: decode_j_jr_class,
    0b0110: decode_cr_class,
    0b0111: decode_alu_32_class,
    0b1011: decode_alu_32_class,
    0b1111: decode_alu_32_class,
}


def decode_instruction(instruction):
    iclass = substring(instruction, 31, 28)
    return DECODERS[iclass](instruction)
