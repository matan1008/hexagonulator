from hexgonulator.common.bits_ops import substring
from ..abstract.transfer_register import TransferRegister


class Q6REqualsR(TransferRegister):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        d = substring(instr, 4, 0)
        s = substring(instr, 20, 16)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        return f'R{self.d}=R{self.s})'
