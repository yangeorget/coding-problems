from typing import List


class KthLargest:
    def __init__(self, k: int, numbers: List[int] = []) -> None:
        self.k = k
        self.numbers: List[int] = []
        for number in numbers:
            self.kth = self.add(number)

    def add(self, new_number: int) -> int:
        self.numbers = [
            *[num for num in self.numbers if num > new_number],
            new_number,
            *[num for num in self.numbers if num <= new_number],
        ][: self.k]
        self.kth = self.numbers[-1] if len(self.numbers) == self.k else None
        return self.kth
