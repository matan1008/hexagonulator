from hexgonulator.common.bits_ops import to_unsigned
from hexgonulator.v67.instructions.instruction import Instruction


class MemhAddImm(Instruction):
    def __init__(self, instr, s, offset, imm):
        super().__init__(instr)
        self.s = s
        self.offset = offset
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.offset
        tmp = processor.mem_get(ea, 2)
        tmp += self.imm
        processor.mem_set(ea, 2, to_unsigned(tmp, 16))
        yield
        yield
