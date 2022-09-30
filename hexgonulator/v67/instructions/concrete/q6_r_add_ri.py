from hexgonulator.common.bits_ops import substring, chain
from ..abstract.add import Add


class Q6RAddRi(Add):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s16_higher = substring(instr, 27, 21)
        s16_lower = substring(instr, 13, 5)
        s16 = apply_extension(chain(s16_higher, s16_lower, 9), 16, signed=True)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm16=s16)

    def __repr__(self):
        return f'R{self.d}=add(R{self.s}, #{self.imm16})'
