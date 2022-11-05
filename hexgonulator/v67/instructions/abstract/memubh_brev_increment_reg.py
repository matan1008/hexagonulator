from hexgonulator.common.bits_ops import substring, to_unsigned, bit_reverse, set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class MemubhBrevIncrementReg(Instruction):
    def __init__(self, instr, d, x, mu):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.mu = mu

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        m = processor.registers.m0 if self.mu == 0b0 else processor.registers.m1
        yield
        ea = set_substring(rx, 15, 0, bit_reverse(substring(rx, 15, 0), 16))
        data = processor.mem_get(ea, 2)
        result = 0
        for i in range(2):
            result = set_substring(result, (i * 16) + 15, i * 16, substring(data, (i * 8) + 7, i * 8))
        yield
        processor.registers.general[self.x] = to_unsigned(rx + m.value, 32)
        self.set_new_value_register(processor, self.d, result)
        yield
