from hexgonulator.common.bits_ops import substring, chain, to_signed, bit_at
from ..abstract.or_ import Or


class Q6ROrRi(Or):
    @classmethod
    def from_int(cls, instr):
        s10_higher = bit_at(instr, 21)
        s10_lower = substring(instr, 13, 5)
        s10 = to_signed(chain(s10_higher, s10_lower, 9), 16)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm10=s10)

    def __repr__(self):
        return f'R{self.d}=or(R{self.s}, #{self.imm10})'
