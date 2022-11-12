from hexgonulator.common.bits_ops import to_unsigned, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewIndirectIncrementReg(Instruction):
    def __init__(self, instr, t, x, mu):
        super().__init__(instr)
        self.t = t
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(rx, 1, nt)
        yield
