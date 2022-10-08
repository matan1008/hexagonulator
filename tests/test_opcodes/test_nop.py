def test_nop(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\x00\x7f')
    hexagon.cycle()
