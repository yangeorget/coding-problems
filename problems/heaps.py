class Heap:
    """
    A heap.
    """

    def __init__(self, size, greater):
        self.greater = greater
        self.values = [None for _ in range(0, size)]
        self.size = 0

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
        if pos > 0:
            father = (pos - 1) >> 1
            if self.greater(self.values[pos], self.values[father]):
                self.swap(pos, father)
                self.up(father)

    def down(self, pos):
        left = (pos << 1) + 1
        if left < self.size:
            right = left + 1
            greatest = (
                right
                if right < self.size
                and self.greater(self.values[right], self.values[left])
                else left
            )
            if self.greater(self.values[greatest], self.values[pos]):
                self.swap(pos, greatest)
                self.down(greatest)


class MaxHeap(Heap):
    def __init__(self, size):
        super().__init__(size, lambda a, b: a > b)


class MinHeap(Heap):
    def __init__(self, size):
        super().__init__(size, lambda a, b: a < b)
