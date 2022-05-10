from problems.maximal_path import MaximalPath, TreeNode


class TestMaximalPath:
    def test_solve0(self) -> None:
        assert MaximalPath().solve(TreeNode(-3)) == -3

    def test_solve2(self) -> None:
        assert MaximalPath().solve(TreeNode(1, TreeNode(2), TreeNode(3))) == 6

    def test_solve1(self) -> None:
        assert MaximalPath().solve(TreeNode(2, TreeNode(-1))) == 2

    def test_solve3(self) -> None:
        assert (
            MaximalPath().solve(
                TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            )
            == 42
        )

    def test_solve4(self) -> None:
        assert (
            MaximalPath().solve(
                TreeNode(
                    -1,
                    TreeNode(-2, TreeNode(-6)),
                    TreeNode(10, TreeNode(-3), TreeNode(-6)),
                )
            )
            == 10
        )
