from hexgonulator.v67.instructions.instruction import Instruction


class ReadUbIndirectWithRegisterOffset(Instruction):
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
        data = processor.mem_get(ea, 1)
        yield
        self.set_new_value_register(processor, self.d, data)
        yield
