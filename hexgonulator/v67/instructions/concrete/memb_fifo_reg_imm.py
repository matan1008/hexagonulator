from hexgonulator.common.bits_ops import substring, chain
from ..abstract.memb_fifo_indirect_with_offset import MembFifoIndirectWithOffset


class MembFifoRegImm(MembFifoIndirectWithOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        y = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        imm_high = substring(instr, 26, 25)
        imm_low = substring(instr, 13, 5)
        imm = apply_extension(chain(imm_high, imm_low, 9), 11, signed=True)
        return cls(instr, y=y, imm=imm, s=s)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memb_fifo(R{self.s}+#{self.imm})'
