from problems.heaps import Heap

MAX_VALUE = 250000000


class MinCostPath:
    def minimum_cost_path(self, grid):
        n = len(grid)
        n1 = n - 1
        visited = [[False for _ in range(0, n)] for _ in range(0, n)]
        values = []
        for i in range(0, n):
            values.append([])
            for j in range(0, n):
                values[-1].append(MAX_VALUE)
        values[0][0] = grid[0][0]
        heap = Heap(n * n, lambda a, b: values[a[0]][a[1]] < values[b[0]][b[1]])
        heap.add((0, 0))
        while heap.size > 0:
            (i, j) = heap.pop()
            visited[i][j] = True
            if i == n1 and j == n1:
                return values[n1][n1]
            if (
                i < n1
                and not visited[i + 1][j]
                and values[i][j] + grid[i + 1][j] < values[i + 1][j]
            ):
                values[i + 1][j] = values[i][j] + grid[i + 1][j]
                heap.add((i + 1, j))
            if (
                j < n1
                and not visited[i][j + 1]
                and values[i][j] + grid[i][j + 1] < values[i][j + 1]
            ):
                values[i][j + 1] = values[i][j] + grid[i][j + 1]
                heap.add((i, j + 1))
            if (
                i > 0
                and not visited[i - 1][j]
                and values[i][j] + grid[i - 1][j] < values[i - 1][j]
            ):
                values[i - 1][j] = values[i][j] + grid[i - 1][j]
                heap.add((i - 1, j))
            if (
                j > 0
                and not visited[i][j - 1]
                and values[i][j] + grid[i][j - 1] < values[i][j - 1]
            ):
                values[i][j - 1] = values[i][j] + grid[i][j - 1]
                heap.add((i, j - 1))
        return MAX_VALUE
