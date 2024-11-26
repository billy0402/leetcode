#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        indegree = [0] * n
        for _, loser in edges:
            indegree[loser] += 1

        champion = -1
        champion_count = 0
        for i, count in enumerate(indegree):
            if count > 0:
                continue
            champion = i
            champion_count += 1

        return champion if champion_count == 1 else -1


# @lc code=end
