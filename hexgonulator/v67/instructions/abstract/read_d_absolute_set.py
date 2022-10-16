from hexgonulator.v67.instructions.instruction import Instruction


class ReadDAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 8)
        yield
        processor.registers.set_general_pair(self.d, data)
        processor.registers.general[self.e] = self.imm
        yield
