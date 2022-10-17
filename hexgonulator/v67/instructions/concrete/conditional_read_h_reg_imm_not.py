from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_read_h_indirect_offset import ConditionalReadHIndirectOffset


class ConditionalReadHRegImmNot(ConditionalReadHIndirectOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        pt = substring(instr, 12, 11)
        imm = apply_extension(substring(instr, 10, 5) << 1, 7, signed=False)
        return cls(instr, d=d, imm=imm, s=s, pt=pt, sense=False)

    def __repr__(self):
        return f'if (!P{self.pt}) R{self.d}=memh(R{self.s}+#{self.imm})'
