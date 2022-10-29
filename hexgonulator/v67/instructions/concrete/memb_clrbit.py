from hexgonulator.common.bits_ops import substring
from ..abstract.memb_clrbit import MembClrbit as _MembClrbit


class MembClrbit(_MembClrbit):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u5 = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        offset = apply_extension(substring(instr, 12, 7), 6, signed=False)
        return cls(instr, imm=u5, s=s, offset=offset)

    def __repr__(self):
        return f'memb(R{self.s}+#{self.offset})=clrbit(#{self.imm})'
