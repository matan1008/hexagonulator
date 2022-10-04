from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_sxth import ConditionalSxth


class ConditionalSxthNotNew(ConditionalSxth):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u2 = substring(instr, 9, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, pu=u2, dot_new=True, sense=False)

    def __repr__(self):
        return f'if (!P{self.pu}.new) R{self.d}=sxth(R{self.s})'
