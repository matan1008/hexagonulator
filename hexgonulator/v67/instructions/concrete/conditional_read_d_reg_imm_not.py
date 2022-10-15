from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_read_d_indirect_offset import ConditionalReadDIndirectOffset


class ConditionalReadDRegImmNot(ConditionalReadDIndirectOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        pt = substring(instr, 12, 11)
        imm = substring(instr, 10, 5) << 3
        imm = apply_extension(imm, 9, signed=False)
        return cls(instr, d=d, imm=imm, s=s, pt=pt, sense=False)

    def __repr__(self):
        return f'if (!P{self.pt}) R{self.d + 1}:{self.d}=memd(R{self.s}+#{self.imm})'
