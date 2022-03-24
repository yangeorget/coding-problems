from problems.siblings import nodes_without_siblings, Node


class TestSiblings:
    def test_no_siblings(self) -> None:
        node = Node(1)
        assert nodes_without_siblings(node) == [-1]
        node = Node(1, Node(2), Node(3))
        assert nodes_without_siblings(node) == [-1]
        node = Node(1, None, Node(3))
        assert nodes_without_siblings(node) == [3]
        node = Node(1, Node(4, Node(2), None), Node(5, None, Node(3)))
        assert nodes_without_siblings(node) == [2, 3]
