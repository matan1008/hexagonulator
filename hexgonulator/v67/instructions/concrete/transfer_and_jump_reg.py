from hexgonulator.common.bits_ops import substring, chain
from ..abstract.transfer_and_jump import TransferAndJump


class TransferAndJumpReg(TransferAndJump):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r9_high = substring(instr, 21, 20)
        r9_low = substring(instr, 7, 1)
        r9 = chain(r9_high, r9_low, 7)
        r = apply_extension(r9 << 2, 11, signed=True)
        d = substring(instr, 11, 8)
        s = substring(instr, 19, 16)
        return cls(instr, r=r, d=d, s=s)

    def __repr__(self):
        return f'R{self.d}=R{self.s} ; jump PC + #{self.r}'
