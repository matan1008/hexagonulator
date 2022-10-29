from hexgonulator.common.bits_ops import substring, chain
from ..abstract.membh_indirect_with_offset import MembhIndirectWithOffset


class MembhRegImm(MembhIndirectWithOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        imm_high = substring(instr, 26, 25)
        imm_low = substring(instr, 13, 5)
        imm = apply_extension(chain(imm_high, imm_low, 9) << 1, 12, signed=True)
        return cls(instr, d=d, imm=imm, s=s)

    def __repr__(self):
        return f'R{self.d}=membh(R{self.s}+#{self.imm})'
