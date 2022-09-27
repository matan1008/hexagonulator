import struct

LENGTH_FORMATS = {
    1: 'B',
    2: '<H',
    4: '<I',
    8: '<Q',
}


def to_int(bytes_: bytes, length: int) -> int:
    return struct.unpack(LENGTH_FORMATS[length], bytes_)[0]


def from_int(int_: int, length: int) -> bytes:
    return struct.pack(LENGTH_FORMATS[length], int_)


class MemoryControllerHub:
    """
    Provides the CPU and memory and input/output devices to interact
    """

    def __init__(self):
        self.controllers = []

    def get_memory_by_address(self, address):
        for memory in self.controllers:
            if memory.start <= address < memory.end:
                return memory

    def __getitem__(self, addr_size) -> int:
        """
        Reads memory as a little endian
        :addr_size: Tuple of address and size in bytes
        :return: data
        """
        (addr, size) = addr_size
        assert size == 1 or size == 2 or size == 4 or size == 8
        mc = self.get_memory_by_address(addr)
        if mc is not None:
            data = mc.mem[addr - mc.start, size]
            return to_int(data, size)
        return 0

    def __setitem__(self, addr_size, value: int):
        """
        Writes memory as a little endian
        :addr_size: Tuple of address and size in bytes
        :value: Bytes to write
        """
        (addr, size) = addr_size
        assert size == 1 or size == 2 or size == 4 or size == 8
        mc = self.get_memory_by_address(addr)
        if mc is not None:
            mc.mem[addr - mc.start, size] = from_int(value, size)
