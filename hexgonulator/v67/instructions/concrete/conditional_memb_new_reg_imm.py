from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.conditional_memb_new_indirect_offset import ConditionalMembNewIndirectOffset


class ConditionalMembNewRegImm(ConditionalMembNewIndirectOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        pv = substring(instr, 1, 0)
        s = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        imm = apply_extension(chain(bit_at(instr, 13), substring(instr, 7, 3), 5), 6, signed=False)
        return cls(instr, t=t, imm=imm, s=s, pv=pv)

    def __repr__(self):
        return f'if (P{self.pv}) memb(R{self.s}+#{self.imm})=N{self.t}.new'
