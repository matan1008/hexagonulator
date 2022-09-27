from hexgonulator.common.bits_ops import set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class TransferImmediateHl(Instruction):
    def __init__(self, instr, x, imm16, high):
        super().__init__(instr)
        self.x = x
        self.imm16 = imm16
        self.high = high

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        yield
        if self.high:
            result = set_substring(rx, 31, 16, self.imm16)
        else:
            result = set_substring(rx, 15, 0, self.imm16)
        yield
        processor.registers.general[self.x] = result
        yield
