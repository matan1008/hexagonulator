from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.cmp_eq_and_jump import CmpEqAndJump


class CmpEqAndJumpP0Minus1Not(CmpEqAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = apply_extension(chain(r9_high, r9_low, 7) << 2, 11, signed=True)
        s = (bit_at(instr, 19) * 16) + substring(instr, 18, 16)
        return cls(instr, r=r9, s=s, pu=0, imm=-1, sense=False)

    def __repr__(self):
        return f'p{self.pu}=cmp.eq(R{self.s},#-1); if (!p{self.pu}.new) jump:nt PC + #{self.r}'
