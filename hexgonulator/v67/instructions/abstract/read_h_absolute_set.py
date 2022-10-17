from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadHAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 2)
        yield
        processor.registers.general[self.d] = sign_extend(data, 16, 32)
        processor.registers.general[self.e] = self.imm
        yield
