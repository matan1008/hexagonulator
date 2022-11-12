from hexgonulator.common.bits_ops import substring, to_signed
from ..abstract.memb_new_indirect_increment_imm import MembNewIndirectIncrementImm


class MembNewIncImm(MembNewIndirectIncrementImm):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        imm = to_signed(substring(instr, 6, 3), 4)
        return cls(instr, imm=imm, x=x, t=t)

    def __repr__(self):
        return f'memb(R{self.x}++#{self.imm})=N{self.t}.new'
