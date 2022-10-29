from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.membh_pair_indirect_increment_reg import MembhPairIndirectIncrementReg


class MembhPairIncReg(MembhPairIndirectIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        mu = bit_at(instr, 13)
        return cls(instr, d=d, x=x, mu=mu)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=membh(R{self.x}++M{self.mu})'