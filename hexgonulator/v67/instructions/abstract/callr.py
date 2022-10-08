from hexgonulator.v67.instructions.instruction import Instruction


class Callr(Instruction):
    def __init__(self, instr, s):
        super().__init__(instr)
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        yield
        processor.registers.lr = processor.registers.npc
        processor.registers.pc = rs
        yield
