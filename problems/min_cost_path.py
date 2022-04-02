from problems.heaps import IndexedHeap

MAX_VALUE = 500 * 500 * 1000


class MinCostPath:
    def minimum_cost_path(self, grid):
        n = len(grid)
        # all the following arrays could be matrices but have been flattened instead
        flat_grid = [grid[v // n][v % n] for v in range(0, n * n)]
        visited = [False for _ in range(0, n * n)]
        values = [MAX_VALUE for _ in range(0, n * n)]
        values[0] = grid[0][0]
        heap = IndexedHeap(
            lambda a, b: values[a] < values[b],
            [v for v in range(0, n * n)],
            [v for v in range(0, n * n)],
        )
        while heap.size > 0:
            v = heap.pop()
            visited[v] = True
            if v == n * n - 1:
                return values[n * n - 1]
            if (
                v + n < n * n
                and not visited[v + n]
                and values[v] + flat_grid[v + n] < values[v + n]
            ):
                values[v + n] = values[v] + flat_grid[v + n]
                heap.up(heap.indices[v + n])
            if (
                (v % n) + 1 < n
                and not visited[v + 1]
                and values[v] + flat_grid[v + 1] < values[v + 1]
            ):
                values[v + 1] = values[v] + flat_grid[v + 1]
                heap.up(heap.indices[v + 1])
            if (
                0 <= v - n
                and not visited[v - n]
                and values[v] + flat_grid[v - n] < values[v - n]
            ):
                values[v - n] = values[v] + flat_grid[v - n]
                heap.up(heap.indices[v - n])
            if (
                0 < (v % n)
                and not visited[v - 1]
                and values[v] + flat_grid[v - 1] < values[v - 1]
            ):
                values[v - 1] = values[v] + flat_grid[v - 1]
                heap.up(heap.indices[v - 1])
        return MAX_VALUE
