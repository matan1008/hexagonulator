from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadBIndirectWithOffset(Instruction):
    def __init__(self, instr, d, s, imm):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.imm
        data = processor.mem_get(ea, 1)
        yield
        processor.registers.general[self.d] = sign_extend(data, 8, 32)
        yield
