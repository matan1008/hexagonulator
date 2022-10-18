from hexgonulator.common.bits_ops import substring, to_signed
from ..abstract.conditional_read_ub_indirect_increment_imm import ConditionalReadUbIndirectIncrementImm


class ConditionalReadUbIncImmNotNew(ConditionalReadUbIndirectIncrementImm):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        t2 = substring(instr, 10, 9)
        imm = to_signed(substring(instr, 8, 5), 4)
        return cls(instr, d=d, imm=imm, x=x, pt=t2, sense=False, dot_new=True)

    def __repr__(self):
        return f'if (!P{self.pt}.new) R{self.d}=memub(R{self.x}++#{self.imm})'