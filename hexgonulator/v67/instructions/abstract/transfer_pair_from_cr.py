from hexgonulator.v67.instructions.instruction import Instruction


class TransferPairFromCr(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        cs = processor.registers.transfer_read_control_register(self.s)
        css = processor.registers.transfer_read_control_register(self.s + 1)
        yield
        yield
        processor.registers.general[self.d] = cs
        processor.registers.general[self.d + 1] = css
        yield
