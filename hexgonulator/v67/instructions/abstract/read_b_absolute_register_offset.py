from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadBAbsoluteRegisterOffset(Instruction):
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
        data = processor.mem_get(ea, 1)
        yield
        self.set_new_value_register(processor, self.d, sign_extend(data, 8, 32))
        yield
