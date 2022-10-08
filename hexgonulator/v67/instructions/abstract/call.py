from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class Call(Instruction):
    def __init__(self, instr, r):
        super().__init__(instr)
        self.r = r

    def execute(self, processor):
        yield
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        processor.registers.lr = processor.registers.npc
        processor.registers.pc = pc
        yield
