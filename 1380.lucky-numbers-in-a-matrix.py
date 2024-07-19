#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        row, column = len(matrix), len(matrix[0])
        row_min_max = -1
        column_max_min = float("inf")

        for x in range(row):
            row_min = min(matrix[x])
            row_min_max = max(row_min_max, row_min)

        for y in range(column):
            column_max = max(matrix[x][y] for x in range(row))
            column_max_min = min(column_max_min, column_max)

        if row_min_max == column_max_min:
            return [row_min_max]
        return []


# @lc code=end
