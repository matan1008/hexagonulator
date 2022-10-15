from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.conditional_read_d_absolute import ConditionalReadDAbsolute


class ConditionalReadDImmNew(ConditionalReadDAbsolute):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm_high = substring(instr, 20, 16)
        imm_low = bit_at(instr, 8)
        d = substring(instr, 4, 0)
        t2 = substring(instr, 10, 9)
        imm = apply_extension(chain(imm_high, imm_low, 1), 6, signed=False)
        return cls(instr, d=d, imm=imm, pt=t2, dot_new=True)

    def __repr__(self):
        return f'if (P{self.pt}.new) R{self.d + 1}:{self.d}=memd(#{self.imm})'
