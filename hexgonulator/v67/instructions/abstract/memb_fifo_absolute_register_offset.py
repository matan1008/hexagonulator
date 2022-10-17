from hexgonulator.v67.instructions.instruction import Instruction


class MembFifoAbsoluteRegisterOffset(Instruction):
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
        tmp_v = processor.mem_get(ea, 1)
        ryy = (ryy >> 8) | (tmp_v << 56)
        yield
        processor.registers.set_general_pair(self.y, ryy)
        yield
