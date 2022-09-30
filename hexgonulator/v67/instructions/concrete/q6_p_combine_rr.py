from hexgonulator.common.bits_ops import substring
from ..abstract.combine_words import CombineWords


class Q6PCombineRr(CombineWords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, reg_high=s, reg_low=t)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=combine(R{self.reg_high}, R{self.reg_low})'
