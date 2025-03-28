#
# @lc app=leetcode id=2503 lang=python3
#
# [2503] Maximum Number of Points From Grid Queries
#

# @lc code=start
from heapq import heappop, heappush

DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        results: list[int] = [0] * len(queries)
        rows, cols = len(grid), len(grid[0])
        min_heap = [(grid[0][0], 0, 0)]  # val, row, col
        visited: set[tuple[int, int]] = {(0, 0)}
        counter = 0

        queue = [(n, i) for i, n in enumerate(queries)]
        queue.sort()

        for limit, i in queue:
            while min_heap and min_heap[0][0] < limit:
                val, row, col = heappop(min_heap)  # pyright: ignore[reportUnusedVariable]
                counter += 1

                for x, y in DIRECTIONS:
                    nr, nc = row + x, col + y
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))

            results[i] = counter

        return results


# @lc code=end
