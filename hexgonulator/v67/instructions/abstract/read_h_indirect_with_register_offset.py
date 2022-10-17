from hexgonulator.common.bits_ops import sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class ReadHIndirectWithRegisterOffset(Instruction):
    def __init__(self, instr, d, s, t, shift):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.shift = shift

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        ea = rs + (rt << self.shift)
        data = processor.mem_get(ea, 2)
        yield
        processor.registers.general[self.d] = sign_extend(data, 16, 32)
        yield
