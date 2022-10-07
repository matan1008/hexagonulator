from hexgonulator.common.bits_ops import substring
from ..abstract.predicate_and import PredicateAnd


class Q6PAndPnp(PredicateAnd):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        t = substring(instr, 9, 8)
        d = substring(instr, 1, 0)
        return cls(instr, s=s, d=d, t=t, neg=True)

    def __repr__(self):
        return f'P{self.d}=and(P{self.t}, !P{self.s})'
