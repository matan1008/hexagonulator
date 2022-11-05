from hexgonulator.v67.instructions.instruction import Instruction


class ReadUbAbsoluteSet(Instruction):
    def __init__(self, instr, d, e, imm):
        super().__init__(instr)
        self.d = d
        self.e = e
        self.imm = imm

    def execute(self, processor):
        yield
        data = processor.mem_get(self.imm, 1)
        yield
        self.set_new_value_register(processor, self.d, data)
        processor.registers.general[self.e] = self.imm
        yield
