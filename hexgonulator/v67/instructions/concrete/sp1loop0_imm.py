from hexgonulator.common.bits_ops import substring, chain
from ..abstract.sp_loop0 import SpLoop0


class Sp1Loop0Imm(SpLoop0):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm_1 = substring(instr, 20, 16)
        imm_2 = substring(instr, 7, 5)
        imm_3 = substring(instr, 1, 0)
        imm = chain(chain(imm_1, imm_2, 3), imm_3, 2)
        r7_high = substring(instr, 12, 8)
        r7_low = substring(instr, 4, 3)
        r7 = chain(r7_high, r7_low, 2)
        r = apply_extension(r7 << 2, 9, signed=True)
        return cls(instr, r=r, imm=imm, sp=1)

    def __repr__(self):
        return f'p3=sp1loop0(PC + #{self.r},#{self.imm})'
