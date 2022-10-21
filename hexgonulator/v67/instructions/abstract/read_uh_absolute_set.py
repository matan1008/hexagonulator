from hexgonulator.v67.instructions.instruction import Instruction


class ReadUhAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 2)
        yield
        processor.registers.general[self.d] = data
        processor.registers.general[self.e] = self.imm
        yield
