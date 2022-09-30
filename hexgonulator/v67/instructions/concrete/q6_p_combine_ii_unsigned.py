from hexgonulator.common.bits_ops import substring, bit_at, chain, to_signed
from ..abstract.combine_words import CombineWords


class Q6PCombineIiUnsigned(CombineWords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u6_low_high = substring(instr, 20, 16)
        u6_low_low = bit_at(instr, 13)
        u6_low = apply_extension(chain(u6_low_high, u6_low_low, 1), 8, signed=False)
        s8_high = to_signed(substring(instr, 12, 5), 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm_high=s8_high, imm_low=u6_low)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=combine(#{self.imm_high}, #{self.imm_low})'
