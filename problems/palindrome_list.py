class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def length(self):
        length = 0
        head = self
        while head:
            length += 1
            head = head.next
        return length


class PalindromeList:
    """
    Check if a linked list is a palindrome.
    See https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
    """

    def check(self, head):
        return self._check(head, head.length())[0]

    def _check(self, head, length):
        if length == 0:
            return True, head
        if length == 1:
            return True, head.next
        is_palindrome, next = self._check(head.next, length - 2)
        return is_palindrome and next.data == head.data, next.next
