from problems.kth_largest import KthLargest


class TestKthLargest:
    def test_add(self) -> None:
        fifth = KthLargest(5, [1, 9, 2, 8, 3, 7, 4, 6])
        assert fifth.numbers == [9, 8, 7, 6, 4]
        assert fifth.kth == 4
        fifth.add(5)
        assert fifth.numbers == [9, 8, 7, 6, 5]
        assert fifth.kth == 5
        fifth.add(7)
        assert fifth.numbers == [9, 8, 7, 7, 6]
        assert fifth.kth == 6
