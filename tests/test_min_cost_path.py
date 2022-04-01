from problems.min_cost_path import MinCostPath


class TestMinCostPath:
    def test_minimum_cost_path0(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [9, 4, 9],
                    [6, 7, 6],
                    [8, 3, 3],
                ]
            )
            == 26
        )

    def test_minimum_cost_path1(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [9, 4, 9, 9],
                    [6, 7, 6, 4],
                    [8, 3, 3, 7],
                    [7, 4, 9, 10],
                ]
            )
            == 43
        )

    def test_minimum_cost_path2(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [4, 4],
                    [3, 7],
                ]
            )
            == 14
        )

    def test_minimum_cost_path3(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [9, 7, 6, 2, 4, 3, 5, 7],
                    [4, 3, 5, 8, 9, 9, 8, 4],
                    [9, 1, 1, 1, 9, 8, 9, 3],
                    [3, 5, 7, 5, 2, 10, 10, 1],
                    [3, 5, 1, 3, 4, 5, 10, 3],
                    [4, 10, 9, 10, 2, 8, 8, 6],
                    [9, 9, 7, 5, 6, 8, 3, 1],
                    [6, 7, 6, 10, 3, 2, 5, 9],
                ]
            )
            == 57
        )

    def test_minimum_cost_path4(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [9, 7, 6, 2, 4],
                    [4, 3, 5, 8, 9],
                    [9, 1, 1, 1, 9],
                    [3, 5, 7, 5, 2],
                    [3, 5, 1, 3, 4],
                ]
            )
            == 30
        )

    def test_minimum_cost_path4(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [9, 7, 6, 2, 4, 3],
                    [4, 3, 5, 8, 9, 9],
                    [9, 1, 1, 1, 9, 8],
                    [3, 5, 7, 5, 2, 10],
                    [3, 5, 1, 3, 4, 5],
                    [4, 10, 9, 10, 2, 8],
                ]
            )
            == 40
        )

    def test_minimum_cost_path5(self):
        assert (
            MinCostPath().minimum_cost_path(
                [
                    [3, 5, 8, 9, 9],
                    [1, 1, 1, 9, 8],
                    [5, 7, 5, 2, 10],
                    [5, 1, 3, 4, 5],
                    [10, 9, 10, 2, 8],
                ]
            )
            == 27
        )

    def test_minimum_cost_path6(self):
        assert (
            MinCostPath().minimum_cost_path(
                [[1, 1, 9, 8], [7, 5, 2, 10], [1, 3, 4, 5], [9, 10, 2, 8]]
            )
            == 23
        )
