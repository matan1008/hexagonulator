from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_zxtb import ConditionalZxtb as _ConditionalZxtb


class ConditionalZxtb(_ConditionalZxtb):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u2 = substring(instr, 9, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, pu=u2)

    def __repr__(self):
        return f'if (P{self.pu}) R{self.d}=zxtb(R{self.s})'
