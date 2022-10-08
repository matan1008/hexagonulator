from hexgonulator.v67.instructions.instruction import Instruction


class TransferPairToCr(Instruction):
    def __init__(self, instr, d, s):
        super().__init__(instr)
        self.d = d
        self.s = s

    def execute(self, processor):
        rs = processor.registers.general[self.s]
        rss = processor.registers.general[self.s + 1]
        yield
        yield
        processor.registers.transfer_write_control_register(self.d, rs)
        processor.registers.transfer_write_control_register(self.d + 1, rss)
        yield
