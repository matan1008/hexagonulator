from hexgonulator.memory.hub import MemoryControllerHub
from .instructions.abstract.constant_extender import ConstantExtender
from .instructions.decoders.decode import decode_instruction
from .registers import Registers
from .sequencer import Sequencer
from .xunits import Xunits
from ..common.bits_ops import set_substring, to_signed


class HexagonV67:
    def __init__(self):
        self.sequencer = Sequencer()
        self.registers = Registers()
        self.xunits = Xunits(self)
        self.memory = MemoryControllerHub()
        self.packet = []

    def mem_get(self, address, length):
        return self.memory[address, length]

    def cycle(self):
        self.registers.npc_to_pc()
        self.packet = []
        for i in range(4):
            instruction_int = self.mem_get(self.registers.pc + (4 * i), 4)
            instr = decode_instruction(instruction_int).from_int(instruction_int, apply_extension=self.apply_extension)
            self.packet.append(instr)
            if instr.parse_field == 0b11:
                break
        self.registers.pc = self.registers.pc + (4 * len(self.packet))
        self.xunits.set_instructions(self.sequencer.sequence(self.packet))
        self.xunits.cycle()
        self.test_loop()

    def test_loop(self):
        if self.packet[0].parse_field == 0b10 and self.packet[1].parse_field == 0b10:
            self.endloop01()
        elif self.packet[0].parse_field == 0b10:
            self.endloop0()
        elif len(self.packet) > 1 and self.packet[1].parse_field == 0b10:
            self.endloop1()

    def endloop0(self):
        if self.registers.usr.lpcfg:
            if self.registers.usr.lpcfg == 0b01:
                self.registers.predicate[3] = 0xff
            self.registers.usr.lpcfg -= 1
        if self.registers.lc0 > 1:
            self.registers.pc = self.registers.sa0
            self.registers.lc0 -= 1

    def endloop01(self):
        if self.registers.usr.lpcfg:
            if self.registers.usr.lpcfg == 0b01:
                self.registers.predicate[3] = 0xff
            self.registers.usr.lpcfg -= 1
        if self.registers.lc0 > 1:
            self.registers.pc = self.registers.sa0
            self.registers.lc0 -= 1
        elif self.registers.lc1 > 1:
            self.registers.pc = self.registers.sa1
            self.registers.lc1 -= 1

    def endloop1(self):
        if self.registers.lc1 > 1:
            self.registers.pc = self.registers.sa1
            self.registers.lc1 -= 1

    def apply_extension(self, bits: int, length: int, signed=False):
        if self.packet and isinstance(self.packet[-1], ConstantExtender):
            bits = set_substring(bits, 31, 6, self.packet[-1].imm26)
            length = 32
        if signed:
            bits = to_signed(bits, length)
        return bits

    def frame_unscramble(self, data):
        return data ^ (self.registers.framekey << 32)
