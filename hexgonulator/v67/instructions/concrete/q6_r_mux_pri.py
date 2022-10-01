from hexgonulator.common.bits_ops import substring
from ..abstract.mux import Mux


class Q6RMuxPri(Mux):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s8 = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        rs = substring(instr, 20, 16)
        u2 = substring(instr, 22, 21)
        return cls(instr, d=d, pu=u2, imm_second=s8, reg_first=rs)

    def __repr__(self):
        return f'R{self.d}=mux(P{self.pu}, R{self.reg_first}, #{self.imm_second})'
