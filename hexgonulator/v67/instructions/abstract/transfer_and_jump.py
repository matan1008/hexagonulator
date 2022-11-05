from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class TransferAndJump(Instruction):
    def __init__(self, instr, r, d, s=None, imm=None):
        super().__init__(instr)
        self.r = r
        self.d = d
        self.s = s
        self.imm = imm

    def execute(self, processor):
        transfer = processor.registers.general[self.s] if self.s is not None else self.imm
        yield
        pc = to_unsigned(processor.registers.pc + self.r, 32)
        yield
        self.set_new_value_register(processor, self.d, transfer)
        processor.registers.pc = pc
        yield
