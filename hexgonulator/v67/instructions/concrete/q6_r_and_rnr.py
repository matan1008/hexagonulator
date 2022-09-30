from hexgonulator.common.bits_ops import substring
from ..abstract.and_not import AndNot


class Q6RAndRnr(AndNot):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t)

    def __repr__(self):
        return f'R{self.d}=and(R{self.t}, ~R{self.s})'
