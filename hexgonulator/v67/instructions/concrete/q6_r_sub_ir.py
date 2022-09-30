from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.sub import Sub


class Q6RSubIr(Sub):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s10_higher = bit_at(instr, 21)
        s10_lower = substring(instr, 13, 5)
        s10 = apply_extension(chain(s10_higher, s10_lower, 9), 10, signed=True)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm10=s10)

    def __repr__(self):
        return f'R{self.d}=sub(#{self.imm10}, R{self.s})'
