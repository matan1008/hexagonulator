from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.memb_new_absolute_register_offset import MembNewAbsoluteRegisterOffset


class MembNewImmRegOff(MembNewAbsoluteRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        shift = chain(bit_at(instr, 13), bit_at(instr, 6), 1)
        imm = apply_extension(substring(instr, 5, 0), 6, signed=False)
        return cls(instr, t=t, u=u, shift=shift, imm=imm)

    def __repr__(self):
        return f'memb(R{self.u}<<#{self.shift}+#{self.imm})=N{self.t}.new'
