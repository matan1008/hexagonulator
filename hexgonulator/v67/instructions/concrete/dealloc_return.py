from hexgonulator.common.bits_ops import substring
from ..abstract.dealloc_return import DeallocReturn as _DeallocReturn


class DeallocReturn(_DeallocReturn):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        if self.d == 30 and self.s == 30:
            return 'dealloc_return'
        return f'R{self.d + 1}:{self.d}=dealloc_return(R{self.s}):raw'
