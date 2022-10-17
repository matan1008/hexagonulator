from hexgonulator.common.bits_ops import substring, to_signed
from ..abstract.memb_fifo_indirect_increment_imm import MembFifoIndirectIncrementImm


class MembFifoIncImm(MembFifoIndirectIncrementImm):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        y = substring(instr, 4, 0)
        imm = to_signed(substring(instr, 8, 5), 4)
        return cls(instr, y=y, imm=imm, x=x)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memb_fifo(R{self.x}++#{self.imm})'
