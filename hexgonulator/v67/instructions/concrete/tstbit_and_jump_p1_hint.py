from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.tstbit_and_jump import TstbitAndJump


class TstbitAndJumpP1Hint(TstbitAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = apply_extension(chain(r9_high, r9_low, 7) << 2, 11, signed=True)
        s = (bit_at(instr, 19) * 16) + substring(instr, 18, 16)
        return cls(instr, r=r9, s=s, pu=1, hint=True)

    def __repr__(self):
        return f'p{self.pu}=tstbit(R{self.s},#0); if (p{self.pu}.new) jump:t PC + #{self.r}'
