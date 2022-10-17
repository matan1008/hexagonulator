from hexgonulator.common.bits_ops import substring, bit_at, to_signed
from ..abstract.memh_fifo_circular_increment import MemhFifoCircularIncrement


class MemhFifoImCirc(MemhFifoCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        imm = to_signed(substring(instr, 8, 5) << 1, 5)
        y = substring(instr, 4, 0)
        return cls(instr, y=y, x=x, imm=imm, mu=u)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memh_fifo(R{self.x}++#{self.imm}:circ(M{self.mu}))'
