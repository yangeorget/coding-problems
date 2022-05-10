from problems.google_lakes import GoogleLakes


class TestGoogleLake:
    def test_up(self) -> None:
        assert GoogleLakes([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]).up(0) == 1

    def test_down(self) -> None:
        assert GoogleLakes([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]).down(8) == 11

    def test_volume(self) -> None:
        assert GoogleLakes([1, 2, 3]).volume() == 0
        assert GoogleLakes([3, 2, 1]).volume() == 0
        assert GoogleLakes([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2]).volume() == 15
