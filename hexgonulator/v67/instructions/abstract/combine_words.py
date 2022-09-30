from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class CombineWords(Instruction):
    def __init__(self, instr, d, reg_high=None, reg_low=None, imm_high=None, imm_low=None):
        super().__init__(instr)
        self.d = d
        self.reg_high = reg_high
        self.reg_low = reg_low
        self.imm_high = imm_high
        self.imm_low = imm_low

    def execute(self, processor):
        low = processor.registers.general[self.reg_low] if self.reg_low is not None else self.imm_low
        high = processor.registers.general[self.reg_high] if self.reg_high is not None else self.imm_high
        yield
        low = to_unsigned(low, 32)
        high = to_unsigned(high, 32)
        yield
        processor.registers.general[self.d] = low
        processor.registers.general[self.d + 1] = high
        yield
