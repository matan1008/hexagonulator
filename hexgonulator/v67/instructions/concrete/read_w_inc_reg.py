from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.read_w_indirect_increment_reg import ReadWIndirectIncrementReg


class ReadWIncReg(ReadWIndirectIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        mu = bit_at(instr, 13)
        return cls(instr, d=d, x=x, mu=mu)

    def __repr__(self):
        return f'R{self.d}=memw(R{self.x}++M{self.mu})'