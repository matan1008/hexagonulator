from hexgonulator.common.bits_ops import lower_chunk
from hexgonulator.v67.instructions.instruction import Instruction


class MembNewIndirectIncrementImm(Instruction):
    def __init__(self, instr, t, x, imm):
        super().__init__(instr)
        self.t = t
        self.x = x
        self.imm = imm

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        yield
        yield
        processor.registers.general[self.x] = rx + self.imm
        nt = lower_chunk(processor.get_new_value_operand(self.t), 8)
        processor.mem_set(rx, 1, nt)
        yield
