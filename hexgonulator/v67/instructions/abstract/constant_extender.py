from hexgonulator.v67.instructions.instruction import Instruction


class ConstantExtender(Instruction):
    def __init__(self, instr, imm26):
        super().__init__(instr)
        self.imm26 = imm26

    def execute(self, processor):
        yield
        yield
        yield
