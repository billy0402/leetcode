#
# @lc app=leetcode id=2285 lang=python3
#
# [2285] Maximum Total Importance of Roads
#

# @lc code=start
class Solution:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        degree = [0] * n
        for x, y in roads:
            degree[x] += 1
            degree[y] += 1
        degree.sort()

        total = 0
        for i, d in enumerate(degree):
            total += (i + 1) * d
        return total


# @lc code=end
