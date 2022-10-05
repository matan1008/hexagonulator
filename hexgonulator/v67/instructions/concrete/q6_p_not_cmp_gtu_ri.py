from hexgonulator.common.bits_ops import substring
from ..abstract.cmp_gtu import CmpGtu


class Q6PNotCmpGtuRi(CmpGtu):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm = apply_extension(substring(instr, 13, 5), 9)
        s = substring(instr, 20, 16)
        d = substring(instr, 1, 0)
        return cls(instr, pu=d, s=s, imm=imm, sense=False)

    def __repr__(self):
        return f'P{self.pu}=!cmp.gtu(R{self.s},#{self.imm})'
