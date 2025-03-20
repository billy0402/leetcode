#
# @lc app=leetcode id=3108 lang=python3
#
# [3108] Minimum Cost Walk in Weighted Graph
#

# @lc code=start
class DSU:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.value = [-1] * n

    def find(self, k: int) -> int:
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]

    def union(self, u: int, v: int, w: int) -> None:
        x = self.find(u)
        y = self.find(v)

        if x != y:  # u and v are same edge, so they should have same root
            self.root[y] = x

        if self.value[x] == -1 and self.value[y] == -1:
            self.value[x] = w
        elif self.value[x] != -1 and self.value[y] == -1:
            self.value[x] = w & self.value[x]
        elif self.value[x] == -1 and self.value[y] != -1:
            self.value[x] = w & self.value[y]
        else:  # self.value[x] != -1 and self.value[y] != -1
            self.value[x] = w & self.value[x] & self.value[y]


class Solution:
    def minimumCost(
        self, n: int, edges: list[list[int]], query: list[list[int]]
    ) -> list[int]:
        dsu = DSU(n)
        for u, v, w in edges:
            dsu.union(u, v, w)

        results: list[int] = []
        for u, v in query:
            x, y = dsu.find(u), dsu.find(v)
            if x == y:  # same root
                results.append(dsu.value[x])
            else:
                results.append(-1)
        return results


# @lc code=end
