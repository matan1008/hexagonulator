from ..abstract.nop import Nop as _Nop


class Nop(_Nop):
    @classmethod
    def from_int(cls, instr):
        return cls(instr)

    def __repr__(self):
        return 'nop'
