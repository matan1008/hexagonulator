from hexgonulator.common.bits_ops import substring, chain
from ..abstract.cmp_eq_new_and_jump import CmpEqNewAndJump


class CmpEqNewJumpRegNot(CmpEqNewAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = apply_extension(chain(r9_high, r9_low, 7) << 2, 11, signed=True)
        s = substring(instr, 18, 16)
        t = substring(instr, 12, 8)
        return cls(instr, r=r9, s=s, t=t, sense=False)

    def __repr__(self):
        return f'if (!cmp.eq(N{self.s}.new,R{self.t})) jump:nt PC + #{self.r}'
