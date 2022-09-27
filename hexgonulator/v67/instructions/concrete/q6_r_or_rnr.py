from hexgonulator.common.bits_ops import substring
from ..abstract.or_not import OrNot


class Q6ROrRnr(OrNot):
    @classmethod
    def from_int(cls, instr):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t)

    def __repr__(self):
        return f'R{self.d}=or(R{self.t}, ~R{self.s})'
