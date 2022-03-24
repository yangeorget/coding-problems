from problems.bst_merge import BstMerge, Node


class TestBstMerge:
    def test_path1(self) -> None:
        root = Node(12, Node(9, Node(6), Node(11)))
        path = BstMerge().path(root)
        assert len(path) == 3
        assert path[0] == root
        assert path[1] == root.left
        assert path[2] == root.left.left

    def test_path2(self) -> None:
        root = Node(4, None, Node(9, Node(6), Node(11)))
        path = BstMerge().path(root)
        assert len(path) == 1
        assert path[0] == root

    def test_path3(self) -> None:
        left_node = Node(15799, None, Node(16268))
        right_node = Node(16969, Node(16963, Node(16960), Node(16964)), Node(16990))
        root = Node(16944, left_node, right_node)
        path = BstMerge().path(root)
        assert len(path) == 2
        assert path[0] == root
        assert path[1] == left_node

    def test_flatten0(self) -> None:
        root = Node(16969, Node(16963, Node(16960), Node(16964)), Node(16990))
        path = BstMerge().path(root)
        assert BstMerge().flatten(path) == [16960, 16963, 16964, 16969, 16990]

    def test_flatten1(self) -> None:
        root = Node(
            16944,
            Node(15799, None, Node(16268)),
            Node(16969, Node(16963, Node(16960), Node(16964)), Node(16990)),
        )
        path = BstMerge().path(root)
        assert BstMerge().flatten(path) == [
            15799,
            16268,
            16944,
            16960,
            16963,
            16964,
            16969,
            16990,
        ]

    def test_merge1(self) -> None:
        root1 = Node(5, Node(3, Node(2), Node(4)), Node(6))
        root2 = Node(2, Node(1), Node(3, None, Node(7, Node(6))))
        assert BstMerge().merge(root1, root2) == [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]

    def test_merge2(self) -> None:
        root1 = Node(6, Node(3, Node(1), Node(5)), Node(10, Node(8)))
        root2 = Node(9, Node(7, Node(4), Node(8)), Node(10, None, Node(12)))
        assert BstMerge().merge(root1, root2) == [
            1,
            3,
            4,
            5,
            6,
            7,
            8,
            8,
            9,
            10,
            10,
            12,
        ]

    def test_merge4(self) -> None:
        root1 = Node(15685)
        root2 = Node(
            16944,
            Node(15799, None, Node(16268)),
            Node(16969, Node(16963, Node(16960), Node(16964)), Node(16990)),
        )
        assert BstMerge().merge(root1, root2) == [
            15685,
            15799,
            16268,
            16944,
            16960,
            16963,
            16964,
            16969,
            16990,
        ]
