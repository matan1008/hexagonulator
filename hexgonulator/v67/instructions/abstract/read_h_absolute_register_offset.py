from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadHAbsoluteRegisterOffset(Instruction):
    def __init__(self, instr, d, t, shift, imm):
        super().__init__(instr)
        self.d = d
        self.t = t
        self.shift = shift
        self.imm = imm

    def execute(self, processor):
        rt = processor.registers.general[self.t]
        yield
        ea = self.imm + (rt << self.shift)
        data = processor.mem_get(ea, 2)
        yield
        processor.registers.general[self.d] = sign_extend(data, 16, 32)
        yield
