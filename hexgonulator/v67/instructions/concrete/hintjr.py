from hexgonulator.common.bits_ops import substring
from ..abstract.hintjr import Hintjr as _Hintjr


class Hintjr(_Hintjr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        return cls(instr, s=s)

    def __repr__(self):
        return f'hintjr(R{self.s})'
