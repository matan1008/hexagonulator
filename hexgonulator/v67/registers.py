from hexgonulator.common.bits_ops import substring, set_substring, lower_chunk
from hexgonulator.v67.core_registers.modifier_register import ModifierRegister
from hexgonulator.v67.core_registers.user_status_register import UserStatusRegister


class Registers:
    def __init__(self):
        self.general = [0x00000000 for _ in range(32)]
        # Loop registers
        self.sa0 = 0x00000000
        self.lc0 = 0x00000000
        self.sa1 = 0x00000000
        self.lc1 = 0x00000000
        # Predicate registers
        self.predicate = [0x00 for _ in range(4)]
        # Modifier registers
        self.m0 = ModifierRegister()
        self.m1 = ModifierRegister()
        # The user status register (USR) stores processor status and control bits that are accessible by user programs.
        self.usr = UserStatusRegister()
        # The Program Counter (PC) register points to the next instruction packet to execute.
        self._pc = 0x00000000
        self.npc = 0x00000000
        # The user general pointer (UGP) register is a general-purpose control register.
        self.ugp = 0x00000000
        # The Global Pointer (GP) is used in GP-relative addressing.
        self.gp = 0x00000000
        # The circular start registers (CS0 - CS1) store the start address of a circular buffer in circular addressing.
        self.cs0 = 0x00000000
        self.cs1 = 0x00000000
        # The cycle count registers (UPCYCLELO - UPCYCLEHI) store a 64-bit value containing the current number of
        # processor cycles executed since the Hexagon processor was last reset.
        self.upcyclelo = 0x00000000
        self.upcyclehi = 0x00000000
        # The frame limit register stores the low address of the memory area reserved for the software stack
        self.framelimit = 0x00000000
        # The frame key register stores the key value that is used to XOR-scramble return addresses when they are
        # stored on the software stack
        self.framekey = 0x00000000

    @property
    def sp(self):
        return self.general[29]

    @sp.setter
    def sp(self, value):
        self.general[29] = value

    @property
    def fp(self):
        return self.general[30]

    @fp.setter
    def fp(self, value):
        self.general[30] = value

    @property
    def lr(self):
        return self.general[31]

    @lr.setter
    def lr(self, value):
        self.general[31] = value

    @property
    def pc(self):
        return self._pc

    @pc.setter
    def pc(self, value):
        self.npc = value

    def npc_to_pc(self):
        self._pc = self.npc

    def transfer_write_control_register(self, d, value):
        if d == 0:
            self.sa0 = value
        elif d == 1:
            self.lc0 = value
        elif d == 2:
            self.sa1 = value
        elif d == 3:
            self.lc1 = value
        elif d == 4:
            for i in range(4):
                self.predicate[i] = substring(value, (i * 8) + 7, i * 8)
        elif d == 5:
            # Reserved
            pass
        elif d == 6:
            self.m0.value = value
        elif d == 7:
            self.m1.value = value
        elif d == 8:
            self.usr.value = value
        elif d == 9:
            # PC is not writeable
            pass
        elif d == 10:
            self.ugp = value
        elif d == 11:
            self.gp = value
        elif d == 12:
            self.cs0 = value
        elif d == 13:
            self.cs1 = value
        elif d == 14:
            self.upcyclelo = value
        elif d == 15:
            self.upcyclehi = value

    def transfer_read_control_register(self, d):
        if d == 0:
            return self.sa0
        if d == 1:
            return self.lc0
        if d == 2:
            return self.sa1
        if d == 3:
            return self.lc1
        if d == 4:
            result = 0
            for i in range(4):
                result = set_substring(result, (i * 8) + 7, i * 8, self.predicate[i])
            return result
        if d == 5:
            # Reserved
            return 0x00000000
        if d == 6:
            return self.m0.value
        if d == 7:
            return self.m1.value
        if d == 8:
            return self.usr.value
        if d == 9:
            return self.pc
        if d == 10:
            return self.ugp
        if d == 11:
            return self.gp
        if d == 12:
            return self.cs0
        if d == 13:
            return self.cs1
        if d == 14:
            return self.upcyclelo
        if d == 15:
            return self.upcyclehi

    def get_general_pair(self, r):
        return set_substring(self.general[r], 63, 32, self.general[r + 1])

    def set_general_pair(self, r, value):
        self.general[r] = lower_chunk(value, 32)
        self.general[r + 1] = substring(value, 63, 32)
