from abc import ABC, abstractmethod


class AbstractMemory(ABC):

    @abstractmethod
    def __init__(self, size):
        self.size = size

    def __getitem__(self, address_size):
        (address, size) = address_size
        return self.read(address, size)

    def __setitem__(self, address_size, value):
        self.write(address_size[0], address_size[1], value)

    @abstractmethod
    def read(self, address, size):
        pass

    @abstractmethod
    def write(self, address, size, value):
        pass
