from hexgonulator.common.bits_ops import substring
from ..abstract.combine_words import CombineWords


class Q6PCombineRi(CombineWords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        s8 = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm_low=s8, reg_high=s)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=combine(R{self.reg_high}, #{self.imm_low})'
