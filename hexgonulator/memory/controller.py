class MemoryController:
    """
    One memory or i/o device
    """

    def __init__(self, mem, start, end):
        self.mem = mem
        self.start = start
        self.end = end
