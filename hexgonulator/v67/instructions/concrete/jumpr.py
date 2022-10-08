from hexgonulator.common.bits_ops import substring
from ..abstract.jumpr import Jumpr as _Jumpr


class Jumpr(_Jumpr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        return cls(instr, s=s)

    def __repr__(self):
        return f'jumpr R{self.s}'
