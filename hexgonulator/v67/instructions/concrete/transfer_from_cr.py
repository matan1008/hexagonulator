from hexgonulator.common.bits_ops import substring
from ..abstract.transfer_from_cr import TransferFromCr as _TransferFromCr


class TransferFromCr(_TransferFromCr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        return f'R{self.d}=C{self.s}'
