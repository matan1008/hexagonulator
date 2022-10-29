from hexgonulator.common.bits_ops import substring
from ..abstract.memh_sub_reg import MemhSubReg as _MemhSubReg


class MemhSubReg(_MemhSubReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        offset = apply_extension(substring(instr, 12, 7) << 1, 7, signed=False)
        return cls(instr, t=t, s=s, offset=offset)

    def __repr__(self):
        return f'memh(R{self.s}+#{self.offset})-=R{self.t}'
