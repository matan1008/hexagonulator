from hexgonulator.common.bits_ops import substring, bit_at, to_signed
from ..abstract.read_ub_circular_increment import ReadUbCircularIncrement


class Q6RMemubImCirc(ReadUbCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        imm = to_signed(substring(instr, 8, 5), 4)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, x=x, imm=imm, mu=u)

    def __repr__(self):
        return f'R{self.d}=memub(R{self.x}++#{self.imm}:circ(M{self.mu}))'
