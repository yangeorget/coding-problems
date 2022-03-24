from problems.subset_product import SubsetProduct


class TestSubsetsProduct:
    def test_numOfSubsets(self) -> None:
        assert SubsetProduct().count([], 0, 12) == 0
        assert SubsetProduct().count([5], 1, 12) == 1
        assert SubsetProduct().count([2, 5], 2, 12) == 3
        assert SubsetProduct().count([2, 4, 5, 3], 4, 12) == 8
