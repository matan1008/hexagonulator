from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.memb_new_indirect_increment_reg import MembNewIndirectIncrementReg


class MembNewIncReg(MembNewIndirectIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        mu = bit_at(instr, 13)
        return cls(instr, t=t, x=x, mu=mu)

    def __repr__(self):
        return f'memb(R{self.x}++M{self.mu})=N{self.t}.new'
