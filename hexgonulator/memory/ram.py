from .abstract import AbstractMemory


class RAM(AbstractMemory):
    def __init__(self, size):
        super(RAM, self).__init__(size)
        self.memory_array = bytearray(size)

    def read(self, address, size):
        chunk = self.memory_array[address:address + size]
        return chunk

    def write(self, address, size, value):
        self.memory_array[address:address + size] = value
