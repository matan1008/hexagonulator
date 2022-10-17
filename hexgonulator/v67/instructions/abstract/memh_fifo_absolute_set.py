from hexgonulator.v67.instructions.instruction import Instruction


class MemhFifoAbsoluteSet(Instruction):
    def __init__(self, instr, y, e, imm):
        super().__init__(instr)
        self.y = y
        self.e = e
        self.imm = imm

    def execute(self, processor):
        ryy = processor.registers.get_general_pair(self.y)
        yield
        tmp_v = processor.mem_get(self.imm, 2)
        ryy = (ryy >> 16) | (tmp_v << 48)
        yield
        processor.registers.set_general_pair(self.y, ryy)
        processor.registers.general[self.e] = self.imm
        yield
