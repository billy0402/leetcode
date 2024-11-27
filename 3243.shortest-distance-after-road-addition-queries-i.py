#
# @lc app=leetcode id=3243 lang=python3
#
# [3243] Shortest Distance After Road Addition Queries I
#

# @lc code=start
from collections import deque


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: list[list[int]]
    ) -> list[int]:
        def shortest_path() -> int:
            q = deque(((0, 0),))  # node, length
            visited = {0}

            while q:
                current, length = q.popleft()
                if current == n - 1:
                    return length

                for neighbor in graph[current]:
                    if neighbor in visited:
                        continue
                    q.append((neighbor, length + 1))
                    visited.add(neighbor)

            return 0

        answers: list[int] = []
        graph = [[i + 1] for i in range(n)]
        for src, dst in queries:
            graph[src].append(dst)
            answers.append(shortest_path())
        return answers


# @lc code=end
