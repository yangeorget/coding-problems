class MaxHeap:
    """
    A max heap.
    """

    def __init__(self, values, size):
        self.values = values
        self.size = 0
        for value in values[:size]:
            self.add(value)

    def add(self, value):
        """
        Adds a value to the heap (may throw an exception if capacity is not enough).
        """
        self.values[self.size] = value
        self.up(self.size)
        self.size += 1

    def pop(self):
        self.size -= 1
        self.swap(0, self.size)
        self.down(0)
        return self.values[self.size]

    def swap(self, pos1, pos2):
        tmp = self.values[pos1]
        self.values[pos1] = self.values[pos2]
        self.values[pos2] = tmp

    def up(self, pos):
        if pos > 0 and self.values[pos] > self.values[(pos - 1) // 2]:
            self.swap(pos, (pos - 1) // 2)
            self.up((pos - 1) // 2)

    def down(self, pos):
        if 2 * pos + 1 < self.size and self.values[pos] < self.values[2 * pos + 1]:
            self.swap(pos, 2 * pos + 1)
            self.down(2 * pos + 1)
        elif 2 * pos + 2 < self.size and self.values[pos] < self.values[2 * pos + 2]:
            self.swap(pos, 2 * pos + 2)
            self.down(2 * pos + 2)
