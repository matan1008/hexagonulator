from hexgonulator.common.bits_ops import substring, set_substring, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class MembhPairIndirectIncrementImm(Instruction):
    def __init__(self, instr, d, x, imm):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.imm = imm

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        yield
        data = processor.mem_get(rx, 4)
        result = 0
        for i in range(4):
            extended = sign_extend(substring(data, (i * 8) + 7, i * 8), 8, 16)
            result = set_substring(result, (i * 16) + 15, i * 16, extended)
        yield
        processor.registers.general[self.x] = rx + self.imm
        processor.registers.set_general_pair(self.d, result)
        yield
