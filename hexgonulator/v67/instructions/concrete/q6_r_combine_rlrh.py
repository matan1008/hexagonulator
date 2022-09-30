from hexgonulator.common.bits_ops import substring
from ..abstract.combine_halfwords import CombineHalfwords


class Q6RCombineRlrh(CombineHalfwords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t, t_high=False, s_high=True)

    def __repr__(self):
        return f'R{self.d}=combine(R{self.t}.L, R{self.s}.H)'
