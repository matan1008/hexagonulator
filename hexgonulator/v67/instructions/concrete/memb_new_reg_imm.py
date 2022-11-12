from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.memb_new_indirect_with_offset import MembNewIndirectWithOffset


class MembNewRegImm(MembNewIndirectWithOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 10, 8)
        s = substring(instr, 20, 16)
        imm_1 = substring(instr, 26, 25)
        imm_2 = bit_at(instr, 13)
        imm_3 = substring(instr, 7, 0)
        imm = apply_extension(chain(chain(imm_1, imm_2, 1), imm_3, 8), 11, signed=True)
        return cls(instr, t=t, imm=imm, s=s)

    def __repr__(self):
        return f'memb(R{self.s}+#{self.imm})=N{self.t}.new'
