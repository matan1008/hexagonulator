def test_hintjr(hexagon):
    hexagon.memory.controllers[0].mem.write(0, 4, b'\x00\xc0\xa0\x52')
    hexagon.cycle()
