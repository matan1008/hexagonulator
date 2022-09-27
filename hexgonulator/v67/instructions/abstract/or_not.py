from hexgonulator.common.bits_ops import bit_not
from hexgonulator.v67.instructions.instruction import Instruction


class OrNot(Instruction):
    def __init__(self, instr, d, s, t):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        result = rt | bit_not(rs, 32)
        yield
        processor.registers.general[self.d] = result
        yield
