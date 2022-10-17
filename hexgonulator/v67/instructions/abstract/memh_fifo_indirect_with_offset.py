from hexgonulator.v67.instructions.instruction import Instruction


class MemhFifoIndirectWithOffset(Instruction):
    def __init__(self, instr, y, s, imm):
        super().__init__(instr)
        self.y = y
        self.s = s
        self.imm = imm

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        ryy = processor.registers.get_general_pair(self.y)
        yield
        ea = rs + self.imm
        tmp_v = processor.mem_get(ea, 2)
        ryy = (ryy >> 16) | (tmp_v << 48)
        yield
        processor.registers.set_general_pair(self.y, ryy)
        yield
