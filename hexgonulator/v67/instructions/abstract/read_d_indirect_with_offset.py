from hexgonulator.v67.instructions.instruction import Instruction


class ReadDIndirectWithOffset(Instruction):
    def __init__(self, instr, d, s, imm):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        ea = rs + self.imm
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.set_general_pair(self.d, data)
        yield
