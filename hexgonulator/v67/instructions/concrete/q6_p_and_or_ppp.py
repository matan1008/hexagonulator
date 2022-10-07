from hexgonulator.common.bits_ops import substring
from ..abstract.predicate_and_or import PredicateAndOr


class Q6PAndOrPpp(PredicateAndOr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        t = substring(instr, 9, 8)
        u = substring(instr, 7, 6)
        d = substring(instr, 1, 0)
        return cls(instr, s=s, d=d, t=t, u=u)

    def __repr__(self):
        return f'P{self.d}=and(P{self.s},or(P{self.t},P{self.u}))'
