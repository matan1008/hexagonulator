from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_xor import ConditionalXor as _ConditionalXor


class ConditionalXor(_ConditionalXor):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        u2 = substring(instr, 6, 5)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, pu=u2, s=s, t=t)

    def __repr__(self):
        return f'if (P{self.pu}) R{self.d}=xor(R{self.s}, R{self.t})'
