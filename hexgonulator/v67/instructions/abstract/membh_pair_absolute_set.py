from hexgonulator.common.bits_ops import set_substring, substring, sign_extend
from hexgonulator.v67.instructions.instruction import Instruction


class MembhPairAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 4)
        result = 0
        for i in range(4):
            extended = sign_extend(substring(data, (i * 8) + 7, i * 8), 8, 16)
            result = set_substring(result, (i * 16) + 15, i * 16, extended)
        yield
        processor.registers.set_general_pair(self.d, result)
        processor.registers.general[self.e] = self.imm
        yield
