from hexgonulator.common.bits_ops import chain, substring, set_substring


class ModifierRegister:
    def __init__(self):
        self.value = 0x00000000

    @property
    def i(self):
        return chain(substring(self.value, 31, 28), substring(self.value, 23, 17), 7)

    @i.setter
    def i(self, value):
        self.value = set_substring(self.value, 31, 28, substring(value, 10, 7))
        self.value = set_substring(self.value, 23, 17, substring(value, 6, 0))

    @property
    def k(self):
        return substring(self.value, 27, 24)

    @property
    def length(self):
        return substring(self.value, 16, 0)

    @length.setter
    def length(self, value):
        self.value = set_substring(self.value, 16, 0, value)
