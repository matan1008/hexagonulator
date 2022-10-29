from hexgonulator.common.bits_ops import substring
from ..abstract.memh_clrbit import MemhClrbit as _MemhClrbit


class MemhClrbit(_MemhClrbit):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        u5 = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        offset = apply_extension(substring(instr, 12, 7) << 1, 7, signed=False)
        return cls(instr, imm=u5, s=s, offset=offset)

    def __repr__(self):
        return f'memh(R{self.s}+#{self.offset})=clrbit(#{self.imm})'
