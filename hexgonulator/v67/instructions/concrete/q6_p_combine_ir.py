from hexgonulator.common.bits_ops import substring
from ..abstract.combine_words import CombineWords


class Q6PCombineIr(CombineWords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        s8 = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm_high=s8, reg_low=s)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=combine(#{self.imm_high}, R{self.reg_low})'
