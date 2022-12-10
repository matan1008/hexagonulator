from hexgonulator.common.bits_ops import substring, to_signed
from ..abstract.conditional_memb_new_indirect_increment_imm import ConditionalMembNewIndirectIncrementImm


class ConditionalMembNewIncImm(ConditionalMembNewIndirectIncrementImm):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        v = substring(instr, 1, 0)
        imm = to_signed(substring(instr, 6, 3), 4)
        return cls(instr, t=t, imm=imm, x=x, pv=v)

    def __repr__(self):
        return f'if (P{self.pv}) memb(R{self.x}++#{self.imm})=N{self.t}.new'
