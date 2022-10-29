from hexgonulator.common.bits_ops import substring, set_substring
from hexgonulator.v67.instructions.instruction import Instruction


class MemubhPairIndirectWithOffset(Instruction):
    def __init__(self, instr, d, s, imm):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.imm
        data = processor.mem_get(ea, 4)
        result = 0
        for i in range(4):
            result = set_substring(result, (i * 16) + 15, i * 16, substring(data, (i * 8) + 7, i * 8))
        yield
        processor.registers.set_general_pair(self.d, result)
        yield
