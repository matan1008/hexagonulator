from hexgonulator.common.bits_ops import lower_chunk, substring
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 8)
        yield
        processor.registers.general[self.d] = lower_chunk(data, 32)
        processor.registers.general[self.d + 1] = substring(data, 63, 32)
        processor.registers.general[self.e] = self.imm
        yield
