from hexgonulator.common.bits_ops import substring, chain
from ..abstract.transfer_immediate_hl import TransferImmediateHl


class Q6RhEqualsI(TransferImmediateHl):
    @classmethod
    def from_int(cls, instr):
        u16_high = substring(instr, 23, 22)
        u16_low = substring(instr, 13, 0)
        u16 = chain(u16_high, u16_low, 14)
        x = substring(instr, 20, 16)
        return cls(instr, x=x, imm16=u16, high=True)

    def __repr__(self):
        return f'R{self.x}.H=#{self.imm16})'
