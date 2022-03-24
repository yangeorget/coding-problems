from problems.palindrome_list import PalindromeList, Node


class TestPalindrome:
    def test_length(self) -> None:
        head = Node(1, Node(2, Node(1)))
        assert head.length() == 3

    def test_check(self) -> None:
        head = Node(1, Node(2, Node(1)))
        assert PalindromeList().check(head)
        head = Node(1, Node(2, Node(1, Node(2))))
        assert not PalindromeList().check(head)
