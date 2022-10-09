from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.conditional_jump import ConditionalJump


class ConditionalJumpNotNew(ConditionalJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r_1 = substring(instr, 23, 22)
        r_2 = substring(instr, 20, 16)
        r_3 = bit_at(instr, 13)
        r_4 = substring(instr, 7, 1)
        r = chain(chain(chain(r_1, r_2, 5), r_3, 1), r_4, 7)
        r = apply_extension(r << 2, 17, signed=True)
        u2 = substring(instr, 9, 8)
        return cls(instr, r=r, pu=u2, sense=False, dot_new=True)

    def __repr__(self):
        return f'if (!P{self.pu}.new) jump:nt PC + #{self.r}'
