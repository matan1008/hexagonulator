from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_read_w_indirect_offset import ConditionalReadWIndirectOffset


class ConditionalReadWRegImm(ConditionalReadWIndirectOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        pt = substring(instr, 12, 11)
        imm = apply_extension(substring(instr, 10, 5) << 2, 8, signed=False)
        return cls(instr, d=d, imm=imm, s=s, pt=pt)

    def __repr__(self):
        return f'if (P{self.pt}) R{self.d}=memw(R{self.s}+#{self.imm})'
