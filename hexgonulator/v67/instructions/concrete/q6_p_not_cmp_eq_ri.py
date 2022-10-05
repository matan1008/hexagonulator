from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.cmp_eq import CmpEq


class Q6PNotCmpEqRi(CmpEq):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm = chain(bit_at(instr, 21), substring(instr, 13, 5), 9)
        imm = apply_extension(imm, 10, signed=True)
        s = substring(instr, 20, 16)
        d = substring(instr, 1, 0)
        return cls(instr, pu=d, s=s, imm=imm, sense=False)

    def __repr__(self):
        return f'P{self.pu}=!cmp.eq(R{self.s},#{self.imm})'
