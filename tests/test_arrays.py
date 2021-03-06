from problems.arrays import Arrays


class TestArrays:
    def test_lis_min_length(self) -> None:
        assert Arrays().lis_length([1, 4, 5, 3, 6, 7]) == 5
        assert Arrays().lis_length([9, 7, 4, 9, 8, 9]) == 3
        assert Arrays().lis_length([1, 2, 5, 3, 1]) == 3
        assert Arrays().lis_length([1, 9, 7, 4, 9, 8, 9]) == 4

    def test_min_ins_and_del(self) -> None:
        assert (
            Arrays().min_ins_and_del([9, 7, 4, 9, 8, 9], [2, 4, 7, 8, 9, 10], 6, 6) == 6
        )
        assert Arrays().min_ins_and_del([1, 2, 5, 3, 1], [1, 3, 5], 5, 3) == 4
        assert Arrays().min_ins_and_del([1, 4], [1, 4], 2, 2) == 0
        assert (
            Arrays().min_ins_and_del(
                [1, 9, 7, 4, 9, 8, 9], [1, 2, 4, 7, 8, 9, 10], 7, 7
            )
            == 6
        )
        assert (
            Arrays().min_ins_and_del([9, 7, 4, 9, 8, 9], [2, 4, 7, 8, 9, 10], 6, 6) == 6
        )
