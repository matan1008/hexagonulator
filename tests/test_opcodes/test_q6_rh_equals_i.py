def test_q6_rh_equals_i(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x34\xd2\x20\x72')
    hexagon.cycle()
    assert hexagon.registers.general[0] == 0x12340000
