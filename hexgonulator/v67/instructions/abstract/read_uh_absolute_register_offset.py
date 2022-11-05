from hexgonulator.v67.instructions.instruction import Instruction


class ReadUhAbsoluteRegisterOffset(Instruction):
    def __init__(self, instr, d, t, shift, imm):
        super().__init__(instr)
        self.d = d
        self.t = t
        self.shift = shift
        self.imm = imm

    def execute(self, processor):
        rt = processor.registers.general[self.t]
        yield
        ea = self.imm + (rt << self.shift)
        data = processor.mem_get(ea, 2)
        yield
        self.set_new_value_register(processor, self.d, data)
        yield
