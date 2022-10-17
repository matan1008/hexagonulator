from hexgonulator.v67.instructions.instruction import Instruction


class MembFifoIndirectWithOffset(Instruction):
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
        tmp_v = processor.mem_get(ea, 1)
        ryy = (ryy >> 8) | (tmp_v << 56)
        yield
        processor.registers.set_general_pair(self.y, ryy)
        yield
