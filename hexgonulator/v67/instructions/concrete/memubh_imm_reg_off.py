from hexgonulator.common.bits_ops import substring, bit_at, chain
from ..abstract.memubh_absolute_register_offset import MemubhAbsoluteRegisterOffset


class MemubhImmRegOff(MemubhAbsoluteRegisterOffset):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        t = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        shift = chain(bit_at(instr, 13), bit_at(instr, 7), 1)
        imm = chain(substring(instr, 11, 8), substring(instr, 6, 5), 2)
        imm = apply_extension(imm, 6, signed=False)
        return cls(instr, t=t, d=d, shift=shift, imm=imm)

    def __repr__(self):
        return f'R{self.d}=memubh(R{self.t}<<#{self.shift}+#{self.imm})'
