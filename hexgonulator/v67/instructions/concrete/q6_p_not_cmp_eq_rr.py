from hexgonulator.common.bits_ops import substring
from ..abstract.cmp_eq import CmpEq


class Q6PNotCmpEqRr(CmpEq):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 1, 0)
        return cls(instr, pu=d, s=s, t=t, sense=False)

    def __repr__(self):
        return f'P{self.pu}=!cmp.eq(R{self.s},R{self.t})'
