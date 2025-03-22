#
# @lc app=leetcode id=2685 lang=python3
#
# [2685] Count the Number of Complete Components
#

# @lc code=start
class DSU:
    def __init__(self, n: int) -> None:
        self.root = list(range(n))
        self.size = [1] * n
        self.edge_count = [0] * n

    def find(self, k: int) -> int:
        if self.root[k] != k:
            self.root[k] = self.find(self.root[k])
        return self.root[k]

    def union(self, u: int, v: int) -> None:
        x = self.find(u)
        y = self.find(v)

        # u and v are already same component
        if x == y:
            self.edge_count[x] += 1
            return

        # merge smaller component into larger one
        if self.size[x] > self.size[y]:  # merge y into x
            self.root[y] = x
            self.size[x] += self.size[y]
            self.edge_count[x] += self.edge_count[y] + 1
        else:  # merge x into y
            self.root[x] = y
            self.size[y] += self.size[x]
            self.edge_count[y] += self.edge_count[x] + 1


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)

        complete_count = 0
        for node in range(n):
            if dsu.find(node) == node:
                node_count = dsu.size[node]
                expected_edges = (node_count * (node_count - 1)) // 2
                if dsu.edge_count[node] == expected_edges:
                    complete_count += 1
        return complete_count


# @lc code=end
