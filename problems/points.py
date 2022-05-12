import math
from typing import List, Tuple


class Points:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)
        max_points = 0
        vectors = set()
        for i in range(0, len(points) - 1):
            a = points[i]
            for j in range(i + 1, len(points)):
                d = self.get_equation(a, points[j])
                if d not in vectors:
                    vectors.add(d)
                    max_points = max(max_points, self.count(points, i, j, d))
        return max_points

    def count(self, points: List[List[int]], i: int, j: int, d: List[int]):
        count = 2
        for k in range(j+1, len(points)):
            if points[k][0] * d[0] + points[k][1] * d[1] + d[2] == 0:
                count += 1
        return count

    def get_equation(self, a: List[int], b: List[int]) -> Tuple[int, int, int]:
        eq = b[1] - a[1], a[0] - b[0], a[1] * b[0] - a[0] * b[1]
        if eq[0] < 0:
            eq = -eq[0], -eq[1], -eq[2]
        gcd = math.gcd(eq[0], eq[1], eq[2])
        return eq[0] // gcd, eq[1] // gcd, eq[2] // gcd
