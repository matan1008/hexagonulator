from hexgonulator.common.bits_ops import to_unsigned, signed_sat_q, to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class Sub(Instruction):
    def __init__(self, instr, d, s, imm10=None, t=None, sat=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.imm10 = imm10
        self.sat = sat

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        minuend = self.imm10 if self.imm10 is not None else to_signed(processor.registers.general[self.t], 32)
        yield
        result = minuend - rs
        saturated = False
        if self.sat:
            result, saturated = signed_sat_q(result, 32)
        else:
            result = to_unsigned(result, 32)
        yield
        processor.registers.general[self.d] = result
        if self.sat and saturated:
            processor.registers.usr.ovf = 1
        yield
