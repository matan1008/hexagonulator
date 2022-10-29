from hexgonulator.common.bits_ops import substring, chain
from ..abstract.memubh_pair_indirect_with_offset import MemubhPairIndirectWithOffset


class MemubhPairRegImm(MemubhPairIndirectWithOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        imm_high = substring(instr, 26, 25)
        imm_low = substring(instr, 13, 5)
        imm = chain(imm_high, imm_low, 9) << 2
        imm = apply_extension(imm, 13, signed=True)
        return cls(instr, d=d, imm=imm, s=s)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=memubh(R{self.s}+#{self.imm})'
