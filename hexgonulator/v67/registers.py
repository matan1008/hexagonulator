from hexgonulator.common.bits_ops import bit_at, set_bit_at, substring, set_substring


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


class Registers:
    def __init__(self):
        self.general = [0x00000000 for _ in range(32)]
        self.sa0 = 0x00000000
        self.lc0 = 0x00000000
        self.sa1 = 0x00000000
        self.lc1 = 0x00000000
        self.predicate = [0x00 for _ in range(4)]
        # The user status register (USR) stores processor status and control bits that are accessible by user programs.
        self.usr = UserStatusRegister()
        # The Program Counter (PC) register points to the next instruction packet to execute.
        self.pc = 0x00000000
