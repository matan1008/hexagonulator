def test_q6_p_packhl_rr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x02\xc1\x80\xf5')
    hexagon.registers.general[0] = 0x11223344
    hexagon.registers.general[1] = 0x55667788
    hexagon.cycle()
    assert hexagon.registers.general[2] == 0x33447788
    assert hexagon.registers.general[3] == 0x11225566
