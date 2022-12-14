from hexgonulator.common.bits_ops import sign_extend, set_substring, substring
from hexgonulator.v67.instructions.instruction import Instruction


class MembhAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 2)
        result = 0
        for i in range(2):
            extended = sign_extend(substring(data, (i * 8) + 7, i * 8), 8, 16)
            result = set_substring(result, (i * 16) + 15, i * 16, extended)
        yield
        self.set_new_value_register(processor, self.d, result)
        processor.registers.general[self.e] = self.imm
        yield
