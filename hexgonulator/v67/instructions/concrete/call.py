from hexgonulator.common.bits_ops import substring, chain
from ..abstract.call import Call as _Call


class Call(_Call):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        r22_high = substring(instr, 24, 16)
        r22_low = substring(instr, 13, 1)
        r22 = chain(r22_high, r22_low, 13)
        r = apply_extension(r22 << 2, 24, signed=True)
        return cls(instr, r=r)

    def __repr__(self):
        return f'call PC + #{self.r}'
