from hexgonulator.common.bits_ops import substring
from ..abstract.all8 import All8


class Q6PAll8P(All8):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        d = substring(instr, 1, 0)
        return cls(instr, pd=d, ps=s)

    def __repr__(self):
        return f'P{self.pd}=all8(P{self.ps})'
