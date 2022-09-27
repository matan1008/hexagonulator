from hexgonulator.common.bits_ops import to_unsigned, signed_sat_q
from hexgonulator.v67.instructions.instruction import Instruction


class Add(Instruction):
    def __init__(self, instr, d, s, imm16=None, t=None, sat=False):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.imm16 = imm16
        self.sat = sat

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        addend = self.imm16 if self.imm16 is not None else processor.registers.general[self.t]
        yield
        result = rs + addend
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
