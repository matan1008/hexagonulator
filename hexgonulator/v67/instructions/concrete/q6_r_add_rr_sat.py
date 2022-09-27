from hexgonulator.common.bits_ops import substring, chain, to_signed
from ..abstract.add import Add


class Q6RAddRrSat(Add):
    @classmethod
    def from_int(cls, instr):
        s = substring(instr, 20, 16)
        t = substring(instr, 12, 8)
        d = substring(instr, 4, 0)
        return cls(instr, d=d, s=s, t=t, sat=True)

    def __repr__(self):
        return f'R{self.d}=add(R{self.s}, R{self.t}):sat'
