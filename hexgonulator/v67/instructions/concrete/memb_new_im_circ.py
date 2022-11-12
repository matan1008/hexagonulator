from hexgonulator.common.bits_ops import substring, bit_at, to_signed
from ..abstract.memb_new_circular_increment import MembNewCircularIncrement


class MembNewImCirc(MembNewCircularIncrement):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        u = bit_at(instr, 13)
        imm = to_signed(substring(instr, 6, 3), 4)
        t = substring(instr, 10, 8)
        return cls(instr, t=t, x=x, imm=imm, mu=u)

    def __repr__(self):
        return f'memb(R{self.x}++#{self.imm}:circ(M{self.mu}))=N{self.t}.new'
