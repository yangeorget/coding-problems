from problems.scc import SCC


class TestSCC:
    def test_compute_scc0(self) -> None:
        assert (
            SCC().compute_sccs(
                4,
                [[2, 3], [0], [1], [1]],
            )
            == [[0, 1, 2, 3]]
        )

    def test_compute_scc1(self) -> None:
        assert SCC().compute_sccs(7, [[5, 6], [], [0], [], [], [2], [2]]) == [
            [0, 2, 5, 6],
            [1],
            [3],
            [4],
        ]

    def test_compute_scc2(self) -> None:
        assert SCC().compute_sccs(3, [[1], [2], [0]]) == [
            [0, 1, 2],
        ]
        assert SCC().compute_sccs(5, [[2, 3], [0], [1], [4], []]) == [
            [0, 1, 2],
            [3],
            [4],
        ]
        assert SCC().compute_sccs(6, [[2], [0], [1], [2, 4], [5], [3]]) == [
            [0, 1, 2],
            [3, 4, 5],
        ]
        assert SCC().compute_sccs(2, [[], [0]]) == [
            [0],
            [1],
        ]
        assert SCC().compute_sccs(
            10,
            [[], [3], [1], [0, 8, 9], [5], [3, 4], [], [3], [5, 6], [5]],
        ) == [
            [0],
            [1],
            [2],
            [3, 4, 5, 8, 9],
            [6],
            [7],
        ]
