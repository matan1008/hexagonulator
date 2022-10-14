from hexgonulator.common.bits_ops import lower_chunk, substring
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDIndirectWithOffset(Instruction):
    def __init__(self, instr, d, s, imm):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.imm
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.general[self.d] = lower_chunk(data, 32)
        processor.registers.general[self.d + 1] = substring(data, 63, 32)
        yield
