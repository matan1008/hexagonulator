from hexgonulator.common.bits_ops import substring, chain
from ..abstract.membh_absolute_set import MembhAbsoluteSet


class MembhSetImm(MembhAbsoluteSet):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        e = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        imm_high = substring(instr, 11, 8)
        imm_low = substring(instr, 6, 5)
        imm = apply_extension(chain(imm_high, imm_low, 2), 6, signed=False)
        return cls(instr, d=d, imm=imm, e=e)

    def __repr__(self):
        return f'R{self.d}=membh(R{self.e}=#{self.imm})'
