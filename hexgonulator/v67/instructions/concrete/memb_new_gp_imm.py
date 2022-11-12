from hexgonulator.common.bits_ops import substring, chain, bit_at
from ..abstract.memb_new_global_pointer_relative import MembNewGlobalPointerRelative


class MembNewGpImm(MembNewGlobalPointerRelative):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 10, 8)
        imm_1 = substring(instr, 26, 25)
        imm_2 = substring(instr, 20, 16)
        imm_3 = bit_at(instr, 13)
        imm_4 = substring(instr, 7, 0)
        original_imm = chain(chain(chain(imm_1, imm_2, 5), imm_3, 1), imm_4, 8)
        imm = apply_extension(original_imm, 16, signed=False)
        return cls(instr, t=t, imm=imm, use_gp=original_imm == imm)

    def __repr__(self):
        gp = 'gp+' if self.use_gp else ''
        return f'memb({gp}#{self.imm})=N{self.t}.new'
