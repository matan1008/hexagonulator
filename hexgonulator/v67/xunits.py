class Xunits:
    def __init__(self, processor):
        self.processor = processor
        self.units = [None, None, None, None]

    def set_instructions(self, sequenced_instructions):
        self.units = [None if instr is None else instr.execute(self.processor) for instr in sequenced_instructions]

    def cycle(self):
        for _ in range(3):
            for unit in self.units[::-1]:
                if unit is None:
                    continue
                next(unit)
