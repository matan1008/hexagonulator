from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class Loop1(Instruction):
    def __init__(self, instr, r, s=None, imm=None):
        super().__init__(instr)
        self.r = r
        self.s = s
        self.imm = imm

    def execute(self, processor):
        count = processor.registers.general[self.s] if self.s is not None else self.imm
        yield
        sa = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        processor.registers.sa1 = sa
        processor.registers.lc1 = count
        yield
