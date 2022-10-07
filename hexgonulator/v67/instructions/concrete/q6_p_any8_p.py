from hexgonulator.common.bits_ops import substring
from ..abstract.any8 import Any8


class Q6PAny8P(Any8):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        d = substring(instr, 1, 0)
        return cls(instr, pd=d, ps=s)

    def __repr__(self):
        return f'P{self.pd}=any8(P{self.ps})'
