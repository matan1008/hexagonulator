from hexgonulator.v67.instructions.instruction import Instruction


class MemwSetbit(Instruction):
    def __init__(self, instr, s, offset, imm):
        super().__init__(instr)
        self.s = s
        self.offset = offset
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.offset
        tmp = processor.mem_get(ea, 4)
        tmp |= 1 << self.imm
        processor.mem_set(ea, 4, tmp)
        yield
        yield
