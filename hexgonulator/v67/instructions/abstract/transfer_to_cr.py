from hexgonulator.v67.instructions.instruction import Instruction


class TransferToCr(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        yield
        yield
        processor.registers.transfer_write_control_register(self.d, rs)
        yield
