from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.memubh_circular_increment import MemubhCircularIncrement


class MemubhMCirc(MemubhCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, x=x, mu=u)

    def __repr__(self):
        return f'R{self.d}=memubh(R{self.x}++I:circ(M{self.mu}))'
