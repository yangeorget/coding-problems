from problems.max_heap import MaxHeap


class TestMaxHeap:
    def test_heap1(self) -> None:
        heap = MaxHeap([1, 2, 3, 4], 4)
        assert heap.size == 4
        assert heap.values == [4, 3, 2, 1]

    def test_heap2(self) -> None:
        heap = MaxHeap([1, 2, 3, 4, 5], 5)
        assert heap.size == 5
        assert heap.values == [5, 4, 2, 1, 3]
        assert heap.pop() == 5
        assert heap.size == 4
        assert heap.values == [4, 3, 2, 1, 5]
