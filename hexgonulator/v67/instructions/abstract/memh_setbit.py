from hexgonulator.v67.instructions.instruction import Instruction


class MemhSetbit(Instruction):
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
        tmp |= 1 << self.imm
        processor.mem_set(ea, 2, tmp)
        yield
        yield
