from hexgonulator.common.bits_ops import substring
from ..abstract.packhl import Packhl


class Q6PPackhlRr(Packhl):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, dd=d, s=s, t=t)

    def __repr__(self):
        return f'R{self.dd + 1}:{self.dd}=packhl(R{self.s}, R{self.t})'
