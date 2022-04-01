from problems.heaps import MaxHeap, MinHeap


class TestHeaps:
    def test_max_heap1(self) -> None:
        heap = MaxHeap(4)
        heap.add(1)
        heap.add(2)
        heap.add(3)
        heap.add(4)
        assert heap.size == 4
        assert heap.values == [4, 3, 2, 1]

    def test_max_heap2(self) -> None:
        heap = MaxHeap(5)
        heap.add(1)
        heap.add(2)
        heap.add(3)
        heap.add(4)
        heap.add(5)
        assert heap.size == 5
        assert heap.values == [5, 4, 2, 1, 3]
        assert heap.pop() == 5
        assert heap.size == 4
        assert heap.values == [4, 3, 2, 1, 5]

    def test_min_heap1(self) -> None:
        heap = MinHeap(5)
        heap.add(1)
        heap.add(2)
        heap.add(3)
        heap.add(4)
        heap.add(5)
        assert heap.size == 5
        assert heap.values == [1, 2, 3, 4, 5]
        assert heap.pop() == 1
        assert heap.size == 4
        assert heap.values == [2, 4, 3, 5, 1]
