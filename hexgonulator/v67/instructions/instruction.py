from abc import abstractmethod, ABC

from hexgonulator.common.bits_ops import substring


class Instruction(ABC):
    def __init__(self, instr):
        self.instr = instr
        self.new_value_destination_register = None

    @classmethod
    def from_int(cls, instr, apply_extension=None):
        pass

    @property
    def iclass(self):
        return substring(self.instr, 31, 28)

    @property
    def parse_field(self):
        return substring(self.instr, 15, 14)

    @abstractmethod
    def execute(self, processor):
        """
        Execute the opcode on the given processor
        :param processor: Processor to run opcode on.
        """

    def set_new_value_register(self, processor, register: int, value: int):
        self.new_value_destination_register = register
        processor.registers.general[register] = value
