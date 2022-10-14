from hexgonulator.common.bits_ops import lower_chunk, substring, to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDIndirectIncrementReg(Instruction):
    def __init__(self, instr, d, x, mu):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        data = processor.mem_get(rx, 8)
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        processor.registers.general[self.d] = lower_chunk(data, 32)
        processor.registers.general[self.d + 1] = substring(data, 63, 32)
        yield
