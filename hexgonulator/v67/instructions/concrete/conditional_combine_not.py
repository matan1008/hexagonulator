from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_combine import ConditionalCombine


class ConditionalCombineNot(ConditionalCombine):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        u2 = substring(instr, 6, 5)
        dd = substring(instr, 4, 0)
        return cls(instr, dd=dd, pu=u2, s=s, t=t, sense=False)

    def __repr__(self):
        return f'if (!P{self.pu}) R{self.dd + 1}:{self.dd}=combine(R{self.s}, R{self.t})'
