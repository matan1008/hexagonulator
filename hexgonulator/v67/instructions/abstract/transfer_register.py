from hexgonulator.v67.instructions.instruction import Instruction


class TransferRegister(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        yield
        processor.registers.general[self.d] = rs
        yield
