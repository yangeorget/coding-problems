class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def nodes_without_siblings(root):
    """
    See https://practice.geeksforgeeks.org/problems/print-all-nodes-that-dont-have-sibling/1/
    """
    acc = []
    _nodes_without_siblings(acc, root)
    if len(acc) == 0:
        return [-1]
    else:
        return sorted(acc)


def _nodes_without_siblings(acc, node):
    if node.left:
        _nodes_without_siblings(acc, node.left)
        if not node.right:
            acc.append(node.left.data)
    if node.right:
        _nodes_without_siblings(acc, node.right)
        if not node.left:
            acc.append(node.right.data)
