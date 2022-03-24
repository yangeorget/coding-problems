class Node:
    def __init__(self, val, left=None, right=None):
        self.right = right
        self.data = val
        self.left = left


class BstMerge:
    """
    Given two BSTs, return elements of both BSTs in sorted form.
    See https://practice.geeksforgeeks.org/problems/merge-two-bst-s/1/.
    """

    def path(self, root):
        """
        Builds an inorder bst traversal path (without recursion).
        """
        acc = []
        self._path(acc, root)
        return acc

    def _path(self, acc, root):
        if root:
            acc.append(root)
            self._path(acc, root.left)

    def flatten(self, path):
        """
        Flattens a bst based on its traversal path.
        """
        acc = []
        self._flatten(acc, path)
        return acc

    def _flatten(self, acc, path):
        if len(path):
            self._flatten(acc, path[1:])
            acc.append(path[0].data)
            if path[0].right:
                self._flatten(acc, self.path(path[0].right))

    def merge(self, bst1, bst2):
        """
        Main function.
        """
        acc = []
        self._merge(acc, self.path(bst1), self.path(bst2))
        return acc

    def _merge(self, acc, path1, path2):
        while True:
            if not path1:
                return self._flatten(acc, path2)
            if not path2:
                return self._flatten(acc, path1)
            if path1[-1].data <= path2[-1].data:
                acc.append(path1[-1].data)
                self.explore_right(path1)
            else:
                acc.append(path2[-1].data)
                self.explore_right(path2)

    def explore_right(self, path):
        head = path.pop()
        self._path(path, head.right)
