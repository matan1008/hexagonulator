from hexgonulator.common.bits_ops import substring
from ..abstract.transfer_pair_from_cr import TransferPairFromCr as _TransferPairFromCr


class TransferPairFromCr(_TransferPairFromCr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        return f'R{self.d + 1}:{self.d}=C{self.s + 1}:{self.s}'
