from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_jumpr import ConditionalJumpr


class ConditionalJumprNewHint(ConditionalJumpr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u2 = substring(instr, 9, 8)
        return cls(instr, s=s, pu=u2, dot_new=True, direction_hint=True)

    def __repr__(self):
        return f'if (P{self.pu}.new) jumpr:t R{self.s}'
