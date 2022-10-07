from hexgonulator.common.bits_ops import substring
from ..abstract.add_to_pc import AddToPc as _AddToPc


class AddToPc(_AddToPc):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        imm = apply_extension(substring(instr, 12, 7), 6)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm=imm)

    def __repr__(self):
        return f'R{self.d}=add(pc,#{self.imm})'
