from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_dealloc_return import ConditionalDeallocReturn as _ConditionalDeallocReturn


class ConditionalDeallocReturn(_ConditionalDeallocReturn):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        pv = substring(instr, 9, 8)
        d = substring(instr, 4, 0)
        return cls(instr, s=s, d=d, pv=pv)

    def __repr__(self):
        return f'if (P{self.pv}) R{self.d + 1}:{self.d}=dealloc_return(R{self.s}):raw'
