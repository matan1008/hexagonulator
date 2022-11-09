from hexgonulator.common.bits_ops import substring, chain
from ..abstract.cmp_gt_new_and_jump import CmpGtNewAndJump


class CmpGtNewJumpMinus1(CmpGtNewAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = apply_extension(chain(r9_high, r9_low, 7) << 2, 11, signed=True)
        s = substring(instr, 18, 16)
        return cls(instr, r=r9, s=s, imm=-1)

    def __repr__(self):
        return f'if (cmp.gt(N{self.s}.new,#-1)) jump:nt PC + #{self.r}'
