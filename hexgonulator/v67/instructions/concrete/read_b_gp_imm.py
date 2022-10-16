from hexgonulator.common.bits_ops import substring, chain
from ..abstract.read_b_global_pointer_relative import ReadBGlobalPointerRelative


class ReadBGpImm(ReadBGlobalPointerRelative):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        imm_1 = substring(instr, 26, 25)
        imm_2 = substring(instr, 20, 16)
        imm_3 = substring(instr, 13, 5)
        original_imm = chain(chain(imm_1, imm_2, 5), imm_3, 9)
        imm = apply_extension(original_imm, 16, signed=False)
        return cls(instr, d=d, imm=imm, use_gp=original_imm == imm)

    def __repr__(self):
        gp = 'gp+' if self.use_gp else ''
        return f'R{self.d}=memb({gp}#{self.imm})'
