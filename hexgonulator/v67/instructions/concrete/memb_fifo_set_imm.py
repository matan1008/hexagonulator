from hexgonulator.common.bits_ops import substring, chain
from ..abstract.memb_fifo_absolute_set import MembFifoAbsoluteSet


class MembFifoSetImm(MembFifoAbsoluteSet):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        y = substring(instr, 4, 0)
        e = substring(instr, 20, 16)
        imm_high = substring(instr, 11, 8)
        imm_low = substring(instr, 6, 5)
        imm = apply_extension(chain(imm_high, imm_low, 2), 6, signed=False)
        return cls(instr, y=y, imm=imm, e=e)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memb_fifo(R{self.e}=#{self.imm})'
