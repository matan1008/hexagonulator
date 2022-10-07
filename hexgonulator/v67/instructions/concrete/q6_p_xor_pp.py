from hexgonulator.common.bits_ops import substring
from ..abstract.predicate_xor import PredicateXor


class Q6PXorPp(PredicateXor):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        t = substring(instr, 9, 8)
        d = substring(instr, 1, 0)
        return cls(instr, s=s, d=d, t=t)

    def __repr__(self):
        return f'P{self.d}=xor(P{self.s}, P{self.t})'
