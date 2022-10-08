from hexgonulator.common.bits_ops import substring
from ..abstract.callr import Callr as _Callr


class Callr(_Callr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        return cls(instr, s=s)

    def __repr__(self):
        return f'callr R{self.s}'
