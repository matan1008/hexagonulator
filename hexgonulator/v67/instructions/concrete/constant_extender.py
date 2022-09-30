from hexgonulator.common.bits_ops import substring, chain
from ..abstract.constant_extender import ConstantExtender as _ConstantExtender


class ConstantExtender(_ConstantExtender):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        immext_high = substring(instr, 27, 16)
        immext_low = substring(instr, 13, 0)
        immext = chain(immext_high, immext_low, 14)
        return cls(instr, immext)

    def __repr__(self):
        return f'immext(#{self.imm26})'
