from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.memb_new_indirect_with_register_offset import MembNewIndirectWithRegisterOffset


class MembNewRegRegOff(MembNewIndirectWithRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        u = substring(instr, 12, 8)
        t = substring(instr, 2, 0)
        imm = chain(bit_at(instr, 13), bit_at(instr, 7), 1)
        return cls(instr, s=s, t=t, u=u, shift=imm)

    def __repr__(self):
        return f'memb(R{self.s}+R{self.u}<<#{self.shift})=N{self.t}.new'
