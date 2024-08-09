#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#

# @lc code=start
from collections import defaultdict


class Solution:
    def possibleBipartition(self, n: int, dislikes: list[list[int]]) -> bool:
        def dfs(node: int, color: int) -> bool:
            if colors[node] != -1:
                return colors[node] == color

            colors[node] = color
            for neighbor in graph[node]:  # noqa: SIM110
                if not dfs(neighbor, 1 - color):
                    return False
            return True

        graph: dict[int, set[int]] = defaultdict(set)
        for x, y in dislikes:
            graph[x].add(y)
            graph[y].add(x)

        colors = [-1] * (n + 1)
        for i in range(1, n + 1):  # noqa: SIM110
            if colors[i] == -1 and not dfs(i, 0):
                return False
        return True


# @lc code=end
