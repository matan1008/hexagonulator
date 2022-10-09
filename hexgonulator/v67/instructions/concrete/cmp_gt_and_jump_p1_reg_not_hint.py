from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.cmp_gt_and_jump import CmpGtAndJump


class CmpGtAndJumpP1RegNotHint(CmpGtAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = apply_extension(chain(r9_high, r9_low, 7) << 2, 11, signed=True)
        s = (bit_at(instr, 19) * 16) + substring(instr, 18, 16)
        t = (bit_at(instr, 11) * 16) + substring(instr, 10, 8)
        return cls(instr, r=r9, s=s, pu=1, t=t, sense=False, hint=True)

    def __repr__(self):
        return f'p{self.pu}=cmp.gt(R{self.s},R{self.t}); if (!p{self.pu}.new) jump:t PC + #{self.r}'
