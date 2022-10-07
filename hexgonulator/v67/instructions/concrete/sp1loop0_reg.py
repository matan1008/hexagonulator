from hexgonulator.common.bits_ops import substring, chain
from ..abstract.sp_loop0 import SpLoop0


class Sp1Loop0Reg(SpLoop0):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        r7_high = substring(instr, 12, 8)
        r7_low = substring(instr, 4, 3)
        r7 = chain(r7_high, r7_low, 2)
        r = apply_extension(r7 << 2, 9, signed=True)
        return cls(instr, r=r, s=s, sp=1)

    def __repr__(self):
        return f'p3=sp1loop0(PC + #{self.r},R{self.s})'
