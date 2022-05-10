from typing import List


class GoogleLakes:
    """
    https://techdevguide.withgoogle.com/resources/former-interview-question-volume-of-lakes/#!
    """

    def __init__(self, heights: List[int]) -> None:
        self.heights = heights

    def up(self, index: int) -> int:
        while (
            index + 1 < len(self.heights)
            and self.heights[index + 1] >= self.heights[index]
        ):
            index += 1
        return index

    def down(self, index: int) -> int:
        while (
            index + 1 < len(self.heights)
            and self.heights[index + 1] <= self.heights[index]
        ):
            index += 1
        return index

    def volume(self) -> int:
        indices = []  # locally high bars
        volumes = []  # corresponding volunes
        index = self.up(0)
        indices.append(index)
        volumes.append(0)
        while index < len(self.heights):
            down_index = self.down(index)
            index = self.up(down_index)
            if index == down_index:  # we have reached the end
                break
            while (
                self.heights[indices[-1]] < self.heights[index]
                and len(indices) > 1
                and self.heights[indices[-2]] > self.heights[indices[-1]]
            ):  # looking for the best previous high bar
                indices.pop()
                volumes.pop()
            indices.append(index)
            volume = min(self.heights[indices[-1]], self.heights[indices[-2]]) * (
                indices[-1] - indices[-2] - 1
            )
            for i in range(indices[-2] + 1, indices[-1]):
                volume -= self.heights[i]
            volumes.append(volume)
        return sum(volumes)
