from hexgonulator.common.bits_ops import substring
from ..abstract.vector_average_halfwords import VectorAverageHalfwords


class Q6RVavghRrRnd(VectorAverageHalfwords):
    @classmethod
    def from_int(cls, instr):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t, round_=True)

    def __repr__(self):
        return f'R{self.d}=vavgh(R{self.s}, R{self.t}):rnd'
