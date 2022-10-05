from hexgonulator.common.bits_ops import substring
from ..abstract.cmp_eq import CmpEq


class Q6RNotCmpEqRi(CmpEq):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm = apply_extension(substring(instr, 12, 5), 8, signed=True)
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, imm=imm, sense=False)

    def __repr__(self):
        return f'R{self.d}=!cmp.eq(R{self.s},#{self.imm})'
