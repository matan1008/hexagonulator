from hexgonulator.v67.instructions.instruction import Instruction


class Nop(Instruction):
    def execute(self, processor):
        yield
        yield
        yield
