from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.conditional_read_d_indirect_register_offset import ConditionalReadDIndirectRegisterOffset


class ConditionalReadDRegRegOffNot(ConditionalReadDIndirectRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        pv = substring(instr, 6, 5)
        imm = chain(bit_at(instr, 13), bit_at(instr, 7), 1)
        return cls(instr, s=s, t=t, d=d, shift=imm, pv=pv, sense=False)

    def __repr__(self):
        return f'if (!P{self.pv}) R{self.d + 1}:{self.d}=memd(R{self.s}+R{self.t}<<#{self.shift})'
