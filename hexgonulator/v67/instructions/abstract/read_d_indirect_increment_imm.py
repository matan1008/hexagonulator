from hexgonulator.v67.instructions.instruction import Instruction


class ReadDIndirectIncrementImm(Instruction):
    def __init__(self, instr, d, x, imm):
        super().__init__(instr)
        self.d = d
        self.x = x
        self.imm = imm

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        yield
        data = processor.mem_get(rx, 8)
        yield
        processor.registers.general[self.x] = rx + self.imm
        processor.registers.set_general_pair(self.d, data)
        yield
