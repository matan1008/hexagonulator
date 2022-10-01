from hexgonulator.common.bits_ops import lower_chunk, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class Asrh(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        result = sign_extend(rs >> 16, 16, 32)
        yield
        processor.registers.general[self.d] = result
        yield
