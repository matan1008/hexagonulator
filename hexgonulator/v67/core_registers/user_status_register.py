from hexgonulator.common.bits_ops import set_substring, substring, bit_at, set_bit_at


class UserStatusRegister:
    def __init__(self):
        self.value = 0x00000000

    @property
    def lpcfg(self):
        return substring(self.value, 9, 8)

    @lpcfg.setter
    def lpcfg(self, value):
        self.value = set_substring(self.value, 9, 8, value)

    @property
    def ovf(self):
        return bit_at(self.value, 0)

    @ovf.setter
    def ovf(self, value):
        self.value = set_bit_at(self.value, 0, value)
