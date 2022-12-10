from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.conditional_memb_new_indirect_register_offset import ConditionalMembNewIndirectRegisterOffset


class ConditionalMembNewRegRegOffNot(ConditionalMembNewIndirectRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u = substring(instr, 12, 8)
        t = substring(instr, 2, 0)
        pv = substring(instr, 6, 5)
        imm = chain(bit_at(instr, 13), bit_at(instr, 7), 1)
        return cls(instr, t=t, pv=pv, s=s, u=u, shift=imm, sense=False)

    def __repr__(self):
        return f'if (!P{self.pv}) memb(R{self.s}+R{self.u}<<#{self.shift})=N{self.t}.new'
