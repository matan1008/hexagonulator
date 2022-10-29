from hexgonulator.common.bits_ops import substring, to_signed
from ..abstract.memubh_pair_indirect_increment_imm import MemubhPairIndirectIncrementImm


class MemubhPairIncImm(MemubhPairIndirectIncrementImm):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        imm = to_signed(substring(instr, 8, 5) << 2, 6)
        return cls(instr, d=d, imm=imm, x=x)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=memubh(R{self.x}++#{self.imm})'
