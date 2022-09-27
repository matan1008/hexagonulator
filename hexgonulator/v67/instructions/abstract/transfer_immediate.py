from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class TransferImmediate(Instruction):
    def __init__(self, instr, d, imm16):
        super().__init__(instr)
        self.d = d
        self.imm16 = imm16

    def execute(self, processor):
        yield
        result = to_unsigned(self.imm16, 32)
        yield
        processor.registers.general[self.d] = result
        yield
