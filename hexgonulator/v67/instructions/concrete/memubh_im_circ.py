from hexgonulator.common.bits_ops import substring, bit_at, to_signed
from ..abstract.memubh_circular_increment import MemubhCircularIncrement


class MemubhImCirc(MemubhCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        imm = to_signed(substring(instr, 8, 5) << 1, 5)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, x=x, imm=imm, mu=u)

    def __repr__(self):
        return f'R{self.d}=memubh(R{self.x}++#{self.imm}:circ(M{self.mu}))'
