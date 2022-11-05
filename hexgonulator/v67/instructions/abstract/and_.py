from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class And(Instruction):
    def __init__(self, instr, d, s, imm10=None, t=None):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.imm10 = imm10

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        arg2 = to_unsigned(self.imm10, 32) if self.imm10 is not None else processor.registers.general[self.t]
        yield
        result = rs & arg2
        yield
        self.set_new_value_register(processor, self.d, result)
        yield
