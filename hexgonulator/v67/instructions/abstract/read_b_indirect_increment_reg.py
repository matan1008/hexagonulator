from hexgonulator.common.bits_ops import to_unsigned, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadBIndirectIncrementReg(Instruction):
    def __init__(self, instr, d, x, mu):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        data = processor.mem_get(rx, 1)
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        self.set_new_value_register(processor, self.d, sign_extend(data, 8, 32))
        yield
