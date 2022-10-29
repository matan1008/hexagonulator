from hexgonulator.common.bits_ops import substring, bit_at, to_signed
from ..abstract.membh_pair_circular_increment import MembhPairCircularIncrement


class MembhPairImCirc(MembhPairCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        imm = to_signed(substring(instr, 8, 5) << 2, 6)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, x=x, imm=imm, mu=u)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=membh(R{self.x}++#{self.imm}:circ(M{self.mu}))'
