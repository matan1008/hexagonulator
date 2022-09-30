from hexgonulator.common.bits_ops import substring, bit_at, chain, to_signed
from ..abstract.combine_words import CombineWords


class Q6PCombineIi(CombineWords):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s8_low_high = substring(instr, 22, 16)
        s8_low_low = bit_at(instr, 13)
        s8_low = to_signed(chain(s8_low_high, s8_low_low, 1), 8)
        s8_high = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm_high=s8_high, imm_low=s8_low)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=combine(#{self.imm_high}, #{self.imm_low})'
