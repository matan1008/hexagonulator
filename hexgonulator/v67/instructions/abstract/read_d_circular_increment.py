from hexgonulator.common.bits_ops import lower_chunk, substring, to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class ReadDCircularIncrement(Instruction):
    def __init__(self, instr, d, x, mu, imm=None):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.imm = imm
        self.mu = mu

    def execute(self, processor):
        ea = processor.registers.general[self.x]
        yield
        m = processor.registers.m0 if self.mu == 0 else processor.registers.m1
        offset = self.imm if self.imm is not None else to_signed(m.i << 3, 14)
        new_pointer = ea + offset
        start_addr = processor.registers.cs0 if self.mu == 0 else processor.registers.cs1
        end_addr = start_addr + m.length
        if new_pointer >= end_addr:
            new_pointer -= m.length
        elif new_pointer < start_addr:
            new_pointer += m.length
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.general[self.x] = new_pointer
        processor.registers.general[self.d] = lower_chunk(data, 32)
        processor.registers.general[self.d + 1] = substring(data, 63, 32)
        yield
