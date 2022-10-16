from hexgonulator.v67.instructions.instruction import Instruction


class ReadDIndirectWithRegisterOffset(Instruction):
    def __init__(self, instr, d, s, t, shift):
        super().__init__(instr)
        self.d = d
        self.s = s
        self.t = t
        self.shift = shift

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rt = processor.registers.general[self.t]
        yield
        ea = rs + (rt << self.shift)
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.set_general_pair(self.d, data)
        yield
