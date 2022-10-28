from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_dealloc_return_new import ConditionalDeallocReturnNew


class ConditionalDeallocReturnNewHint(ConditionalDeallocReturnNew):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        pv = substring(instr, 9, 8)
        d = substring(instr, 4, 0)
        return cls(instr, s=s, d=d, pv=pv, hint=True)

    def __repr__(self):
        return f'if (P{self.pv}.new) R{self.d + 1}:{self.d}=dealloc_return(R{self.s}):t:raw'
