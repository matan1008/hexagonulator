from hexgonulator.common.bits_ops import substring, chain
from ..abstract.conditional_memb_new_absolute import ConditionalMembNewAbsolute


class ConditionalMembNewImmNot(ConditionalMembNewAbsolute):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm_high = substring(instr, 17, 16)
        imm_low = substring(instr, 6, 3)
        t = substring(instr, 10, 8)
        v = substring(instr, 1, 0)
        imm = apply_extension(chain(imm_high, imm_low, 4), 6, signed=False)
        return cls(instr, t=t, imm=imm, pv=v, sense=False)

    def __repr__(self):
        return f'if (!P{self.pv}) memb(#{self.imm})=N{self.t}.new'
