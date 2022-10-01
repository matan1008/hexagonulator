from hexgonulator.common.bits_ops import substring
from ..abstract.mux import Mux


class Q6RMuxPrr(Mux):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        rs = substring(instr, 20, 16)
        rt = substring(instr, 12, 8)
        u2 = substring(instr, 6, 5)
        return cls(instr, d=d, pu=u2, reg_second=rt, reg_first=rs)

    def __repr__(self):
        return f'R{self.d}=mux(P{self.pu}, R{self.reg_first}, R{self.reg_second})'
