from hexgonulator.common.bits_ops import substring
from ..abstract.sxth import Sxth


class Q6RSxthR(Sxth):
    @classmethod
    def from_int(cls, instr):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        return f'R{self.d}=sxth(R{self.s})'
