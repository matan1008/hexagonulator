from hexgonulator.common.bits_ops import substring, bit_at
from ..abstract.memb_new_brev_increment_reg import MembNewBrevIncrementReg


class MembNewIncRegBrev(MembNewBrevIncrementReg):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        x = substring(instr, 20, 16)
        t = substring(instr, 10, 8)
        mu = bit_at(instr, 13)
        return cls(instr, t=t, x=x, mu=mu)

    def __repr__(self):
        return f'memb(R{self.x}++M{self.mu}:brev)=N{self.t}.new'
