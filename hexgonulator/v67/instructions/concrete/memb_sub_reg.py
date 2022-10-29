from hexgonulator.common.bits_ops import substring
from ..abstract.memb_sub_reg import MembSubReg as _MembSubReg


class MembSubReg(_MembSubReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        offset = apply_extension(substring(instr, 12, 7), 6, signed=False)
        return cls(instr, t=t, s=s, offset=offset)

    def __repr__(self):
        return f'memb(R{self.s}+#{self.offset})-=R{self.t}'
