from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_callr import ConditionalCallr as _ConditionalCallr


class ConditionalCallr(_ConditionalCallr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u = substring(instr, 9, 8)
        return cls(instr, s=s, pu=u)

    def __repr__(self):
        return f'if (P{self.pu}) callr R{self.s}'
