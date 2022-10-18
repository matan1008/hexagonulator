from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.read_ub_circular_increment import ReadUbCircularIncrement


class Q6RMemubMCirc(ReadUbCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, x=x, mu=u)

    def __repr__(self):
        return f'R{self.d}=memub(R{self.x}++I:circ(M{self.mu}))'
