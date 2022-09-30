from hexgonulator.common.bits_ops import substring, chain
from ..abstract.transfer_immediate import TransferImmediate


class Q6REqualsI(TransferImmediate):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        i1 = substring(instr, 23, 22)
        i2 = substring(instr, 20, 16)
        i3 = substring(instr, 13, 5)
        s16 = apply_extension(chain(chain(i1, i2, 5), i3, 9), 16, signed=True)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, imm16=s16)

    def __repr__(self):
        return f'R{self.d}=#{self.imm16})'
