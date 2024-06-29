#
# @lc app=leetcode id=2192 lang=python3
#
# [2192] All Ancestors of a Node in a Directed Acyclic Graph
#

# @lc code=start
class Solution:
    def getAncestors(self, n: int, edges: list[list[int]]) -> list[list[int]]:
        def find_ancestors(node: int, visited: set[int]):
            visited.add(node)

            for parent in parents[node]:
                if parent not in visited:
                    find_ancestors(parent, visited)

        parents: list[list[int]] = [[] for _ in range(n)]

        for x, y in edges:
            parents[y].append(x)

        answer: list[list[int]] = []

        for i in range(n):
            ancestors: list[int] = []
            visited: set[int] = set()
            find_ancestors(i, visited)

            for j in range(n):
                if j == i:
                    continue
                if j in visited:
                    ancestors.append(j)

            answer.append(ancestors)

        return answer


# @lc code=end
