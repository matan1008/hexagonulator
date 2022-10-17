from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.memh_fifo_absolute_register_offset import MemhFifoAbsoluteRegisterOffset


class MemhFifoImmRegOff(MemhFifoAbsoluteRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 20, 16)
        y = substring(instr, 4, 0)
        shift = chain(bit_at(instr, 13), bit_at(instr, 7), 1)
        imm = chain(substring(instr, 11, 8), substring(instr, 6, 5), 2)
        imm = apply_extension(imm, 6, signed=False)
        return cls(instr, t=t, y=y, shift=shift, imm=imm)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memh_fifo(R{self.t}<<#{self.shift}+#{self.imm})'
