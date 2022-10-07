from hexgonulator.common.bits_ops import substring
from ..abstract.predicate_not import PredicateNot


class Q6PNotP(PredicateNot):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        d = substring(instr, 1, 0)
        return cls(instr, s=s, d=d)

    def __repr__(self):
        return f'P{self.d}=not(P{self.s})'
