from hexgonulator.common.bits_ops import substring
from ..abstract.transfer_pair_to_cr import TransferPairToCr as _TransferPairToCr


class TransferPairToCr(_TransferPairToCr):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s = substring(instr, 20, 16)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s)

    def __repr__(self):
        return f'C{self.d + 1}:{self.d}=R{self.s + 1}:{self.s}'
