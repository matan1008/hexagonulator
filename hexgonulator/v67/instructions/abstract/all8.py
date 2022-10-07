from hexgonulator.v67.instructions.instruction import Instruction


class All8(Instruction):
    def __init__(self, instr, pd, ps):
        super().__init__(instr)
        self.pd = pd
        self.ps = ps

    def execute(self, processor):
        ps = processor.registers.predicate[self.ps]
        yield
        result = 0xff if ps == 0xff else 0x00
        yield
        processor.registers.predicate[self.pd] = result
        yield
