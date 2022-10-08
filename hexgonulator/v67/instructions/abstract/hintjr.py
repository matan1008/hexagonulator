from hexgonulator.v67.instructions.instruction import Instruction


class Hintjr(Instruction):
    def __init__(self, instr, s):
        super().__init__(instr)
        self.s = s

    def execute(self, processor):
        yield
        yield
        yield
