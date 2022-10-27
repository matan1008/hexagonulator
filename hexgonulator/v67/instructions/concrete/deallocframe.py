from hexgonulator.common.bits_ops import substring
from ..abstract.deallocframe import Deallocframe as _Deallocframe


class Deallocframe(_Deallocframe):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        if self.d == 30 and self.s == 30:
            return 'deallocframe'
        return f'R{self.d + 1}:{self.d}=deallocframe(R{self.s}):raw'
