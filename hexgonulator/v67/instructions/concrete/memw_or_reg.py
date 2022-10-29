from hexgonulator.common.bits_ops import substring
from ..abstract.memw_or_reg import MemwOrReg as _MemwOrReg


class MemwOrReg(_MemwOrReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        offset = apply_extension(substring(instr, 12, 7) << 2, 8, signed=False)
        return cls(instr, t=t, s=s, offset=offset)

    def __repr__(self):
        return f'memw(R{self.s}+#{self.offset})|=R{self.t}'
