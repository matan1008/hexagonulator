from hexgonulator.common.bits_ops import substring, chain, to_signed
from ..abstract.add import Add


class Q6RAddRi(Add):
    @classmethod
    def from_int(cls, instr):
        s16_higher = substring(instr, 27, 21)
        s16_lower = substring(instr, 13, 5)
        s16 = to_signed(chain(s16_higher, s16_lower, 9), 16)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm16=s16)

    def __repr__(self):
        return f'R{self.d}=add(R{self.s}, #{self.imm16})'
