#
# @lc app=leetcode id=2923 lang=python3
#
# [2923] Find Champion I
#

# @lc code=start
class Solution:
    def findChampion(self, grid: list[list[int]]) -> int:
        team = 0
        max_victory = sum(grid[0])

        for i, row in enumerate(grid):
            victory = sum(row)
            if victory > max_victory:
                max_victory = victory
                team = i

        return team


# @lc code=end
