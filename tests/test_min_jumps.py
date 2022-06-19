from problems.min_jumps import MinJumps


class TestMinJumps:
    def test_min_jumps(self):
        assert MinJumps().min_jumps([2, 1, 0, 3], 4) == -1
        assert MinJumps().min_jumps([1, 4, 3, 2, 6, 7], 6) == 2
        assert MinJumps().min_jumps([2, 3, 1, 1, 2, 4, 2, 0, 1, 1], 10) == 4
        assert MinJumps().min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9], 11) == 3
