from hexgonulator.common.bits_ops import substring
from ..abstract.memb_new_absolute_set import MembNewAbsoluteSet


class MembNewSetImm(MembNewAbsoluteSet):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        e = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        imm = apply_extension(substring(instr, 5, 0), 6, signed=False)
        return cls(instr, t=t, imm=imm, e=e)

    def __repr__(self):
        return f'memb(R{self.e}=#{self.imm})=N{self.t}.new'
