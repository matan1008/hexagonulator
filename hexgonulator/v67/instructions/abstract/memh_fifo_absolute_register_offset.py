from hexgonulator.v67.instructions.instruction import Instruction


class MemhFifoAbsoluteRegisterOffset(Instruction):
    def __init__(self, instr, y, t, shift, imm):
        super().__init__(instr)
        self.y = y
        self.t = t
        self.shift = shift
        self.imm = imm

    def execute(self, processor):
        rt = processor.registers.general[self.t]
        ryy = processor.registers.get_general_pair(self.y)
        yield
        ea = self.imm + (rt << self.shift)
        tmp_v = processor.mem_get(ea, 2)
        ryy = (ryy >> 16) | (tmp_v << 48)
        yield
        processor.registers.set_general_pair(self.y, ryy)
        yield
