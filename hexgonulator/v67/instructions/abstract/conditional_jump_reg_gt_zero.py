from hexgonulator.common.bits_ops import to_unsigned, to_signed
from hexgonulator.v67.instructions.instruction import Instruction


class ConditionalJumpRegGtZero(Instruction):
    def __init__(self, instr, r, s, hint=False):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.hint = hint

    def execute(self, processor):
        rs = to_signed(processor.registers.general[self.s], 32)
        yield
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        if rs >= 0:
            processor.registers.pc = pc
        yield
