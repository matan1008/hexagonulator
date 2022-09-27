from hexgonulator.common.bits_ops import sign_extend, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class Sxth(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        result = sign_extend(lower_chunk(rs, 16), 16, 32)
        yield
        processor.registers.general[self.d] = result
        yield
