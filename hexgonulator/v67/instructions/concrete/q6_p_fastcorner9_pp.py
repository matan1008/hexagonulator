from hexgonulator.common.bits_ops import substring
from ..abstract.fastcorner9 import Fastcorner9


class Q6PFastcorner9Pp(Fastcorner9):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 17, 16)
        t = substring(instr, 9, 8)
        d = substring(instr, 1, 0)
        return cls(instr, pd=d, ps=s, pt=t)

    def __repr__(self):
        return f'P{self.pd}=fastcorner9(P{self.ps},P{self.pt})'
