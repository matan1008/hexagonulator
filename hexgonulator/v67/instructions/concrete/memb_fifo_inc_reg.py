from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.memb_fifo_indirect_increment_reg import MembFifoIndirectIncrementReg


class MembFifoIncReg(MembFifoIndirectIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        y = substring(instr, 4, 0)
        mu = bit_at(instr, 13)
        return cls(instr, y=y, x=x, mu=mu)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memb_fifo(R{self.x}++M{self.mu})'
