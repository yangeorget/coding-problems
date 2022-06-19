from problems.binary_search import BinarySearch


class TestBinarySearch:
    def test_binarysearch(self):
        assert BinarySearch().binarysearch([1, 2, 3, 4, 5], 5, 4) == 3
        assert BinarySearch().binarysearch([11, 22, 33, 44, 55], 5, 445) == -1
