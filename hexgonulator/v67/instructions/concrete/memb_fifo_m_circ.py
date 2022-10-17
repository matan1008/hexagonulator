from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.memb_fifo_circular_increment import MembFifoCircularIncrement


class MembFifoMCirc(MembFifoCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        y = substring(instr, 4, 0)
        return cls(instr, y=y, x=x, mu=u)

    def __repr__(self):
        return f'R{self.y + 1}:{self.y}=memb_fifo(R{self.x}++I:circ(M{self.mu}))'
