from hexgonulator.common.bits_ops import substring
from ..abstract.conditional_add import ConditionalAdd


class ConditionalAddNotImm(ConditionalAdd):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u2 = substring(instr, 22, 21)
        s = substring(instr, 20, 16)
        imm = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, pu=u2, imm=imm, sense=False)

    def __repr__(self):
        return f'if (!P{self.pu}) R{self.d}=add(R{self.s},#{self.imm})'
