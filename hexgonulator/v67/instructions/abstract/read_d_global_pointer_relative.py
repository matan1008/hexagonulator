from hexgonulator.v67.instructions.instruction import Instruction


class ReadDGlobalPointerRelative(Instruction):
    def __init__(self, instr, d, imm, use_gp=True):
        super().__init__(instr)
        self.d = d
        self.imm = imm
        self.use_gp = use_gp

    def execute(self, processor):
        gp = processor.registers.gp
        yield
        ea = (gp if self.use_gp else 0) + self.imm
        data = processor.mem_get(ea, 8)
        yield
        processor.registers.set_general_pair(self.d, data)
        yield
