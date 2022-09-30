from hexgonulator.common.bits_ops import substring
from ..abstract.vector_subtract_halfwords import VectorSubtractHalfwords


class Q6RVsubuhRrSat(VectorSubtractHalfwords):
    @classmethod
    def from_int(cls, instr):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t, sat=True, signed=False)

    def __repr__(self):
        return f'R{self.d}=vsubuh(R{self.t}, R{self.s}):sat'
