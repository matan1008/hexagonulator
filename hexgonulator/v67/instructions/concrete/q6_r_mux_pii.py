from hexgonulator.common.bits_ops import substring, bit_at, chain, to_signed
from ..abstract.mux import Mux


class Q6RMuxPii(Mux):
    @classmethod
    def from_int(cls, instr, apply_extension=None):
        s8_second_high = substring(instr, 22, 16)
        s8_second_low = bit_at(instr, 13)
        s8_second = to_signed(chain(s8_second_high, s8_second_low, 1), 8)
        s8_first = apply_extension(substring(instr, 12, 5), 8, signed=True)
        d = substring(instr, 4, 0)
        u1 = substring(instr, 24, 23)
        return cls(instr, d=d, pu=u1, imm_first=s8_first, imm_second=s8_second)

    def __repr__(self):
        return f'R{self.d}=mux(P{self.pu}, #{self.imm_first}, #{self.imm_second})'
