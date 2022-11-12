from hexgonulator.common.bits_ops import substring, to_unsigned, bit_reverse, set_substring, lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewBrevIncrementReg(Instruction):
    def __init__(self, instr, t, x, mu):
        super().__init__(instr)
        self.t = t
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        ea = set_substring(rx, 15, 0, bit_reverse(substring(rx, 15, 0), 16))
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(ea, 1, nt)
        yield
