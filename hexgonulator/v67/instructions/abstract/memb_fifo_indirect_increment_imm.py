from hexgonulator.v67.instructions.instruction import Instruction


class MembFifoIndirectIncrementImm(Instruction):
    def __init__(self, instr, y, x, imm):
        super().__init__(instr)
        self.y = y
        self.x = x
        self.imm = imm

    def execute(self, processor):
        rx = processor.registers.general[self.x]
        ryy = processor.registers.get_general_pair(self.y)
        yield
        tmp_v = processor.mem_get(rx, 1)
        ryy = (ryy >> 8) | (tmp_v << 56)
        yield
        processor.registers.general[self.x] = rx + self.imm
        processor.registers.set_general_pair(self.y, ryy)
        yield
