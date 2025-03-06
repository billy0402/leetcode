#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        rows = len(grid)
        freq: dict[int, int] = {}
        for row in grid:
            for col in row:
                freq[col] = freq.get(col, 0) + 1

        repeated, missing = -1, -1
        for i in range(1, rows**2 + 1):
            if i not in freq:
                missing = i
            elif freq[i] == 2:
                repeated = i
        return [repeated, missing]


# @lc code=end
