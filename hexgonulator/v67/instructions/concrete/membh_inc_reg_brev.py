from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.membh_brev_increment_reg import MembhBrevIncrementReg


class MembhIncRegBrev(MembhBrevIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        mu = bit_at(instr, 13)
        return cls(instr, d=d, x=x, mu=mu)

    def __repr__(self):
        return f'R{self.d}=membh(R{self.x}++M{self.mu}:brev)'
