from hexgonulator.common.bits_ops import substring, set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class MemubhPairAbsoluteRegisterOffset(Instruction):
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
        data = processor.mem_get(ea, 4)
        result = 0
        for i in range(4):
            result = set_substring(result, (i * 16) + 15, i * 16, substring(data, (i * 8) + 7, i * 8))
        yield
        processor.registers.set_general_pair(self.d, result)
        yield
