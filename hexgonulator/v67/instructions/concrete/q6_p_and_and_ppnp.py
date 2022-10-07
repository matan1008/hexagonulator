from hexgonulator.common.bits_ops import substring
from ..abstract.predicate_and_and import PredicateAndAnd


class Q6PAndAndPpnp(PredicateAndAnd):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        t = substring(instr, 9, 8)
        u = substring(instr, 7, 6)
        d = substring(instr, 1, 0)
        return cls(instr, s=s, d=d, t=t, u=u, neg=True)

    def __repr__(self):
        return f'P{self.d}=and(P{self.s},and(P{self.t},!P{self.u}))'
