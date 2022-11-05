from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class AddToPc(Instruction):
    def __init__(self, instr, d, imm):
        super().__init__(instr)
        self.imm = imm
        self.d = d

    def execute(self, processor):
        pc = processor.registers.pc
        yield
        result = to_unsigned(pc + self.imm, 32)
        yield
        self.set_new_value_register(processor, self.d, result)
        yield
