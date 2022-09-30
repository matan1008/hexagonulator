from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.and_ import And


class Q6RAndRi(And):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s10_higher = bit_at(instr, 21)
        s10_lower = substring(instr, 13, 5)
        s10 = apply_extension(chain(s10_higher, s10_lower, 9), 16, signed=True)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm10=s10)

    def __repr__(self):
        return f'R{self.d}=and(R{self.s}, #{self.imm10})'
