from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.conditional_jump_reg_not_zero import ConditionalJumpRegNotZero as _ConditionalJumpRegNotZero


class ConditionalJumpRegNotZero(_ConditionalJumpRegNotZero):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r13_1 = bit_at(instr, 21)
        r13_2 = bit_at(instr, 13)
        r13_3 = substring(instr, 11, 1)
        r13 = chain(chain(r13_1, r13_2, 1), r13_3, 11)
        r = apply_extension(r13 << 2, 15, signed=True)
        s5 = substring(instr, 20, 16)
        return cls(instr, r=r, s=s5)

    def __repr__(self):
        return f'if (R{self.s}!=#0) jump:nt PC + #{self.r}'
