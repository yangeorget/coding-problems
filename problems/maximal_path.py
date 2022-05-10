from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class MaximalPath:
    def solve(self, root: Optional[TreeNode]) -> int:
        max_end, max_inner = self._solve(root)
        return max(max_end, max_inner)

    def _solve(self, root: Optional[TreeNode]) -> Optional[Tuple[int, int]]:
        if root is None:
            return None
        if root.left and root.right:
            max_left_end, max_left_inner = self._solve(root.left)
            max_right_end, max_right_inner = self._solve(root.right)
            max_end = root.val + max(max_left_end, max_right_end, 0)
            max_inner = max(
                max_left_inner,
                max_right_inner,
                max_left_end + root.val + max_right_end,
                max_end,
            )
        elif root.left:
            max_left_end, max_left_inner = self._solve(root.left)
            max_end = root.val + max(max_left_end, 0)
            max_inner = max(max_left_inner, max_end)
        elif root.right:
            max_right_end, max_right_inner = self._solve(root.right)
            max_end = root.val + max(max_right_end, 0)
            max_inner = max(max_right_inner, max_end)
        else:
            max_end = root.val
            max_inner = root.val
        return max_end, max_inner
