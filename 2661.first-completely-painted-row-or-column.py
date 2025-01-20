#
# @lc app=leetcode id=2661 lang=python3
#
# [2661] First Completely Painted Row or Column
#

# @lc code=start
class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_count, col_count = [0] * rows, [0] * cols
        positions: dict[int, tuple[int, int]] = {}

        for row in range(rows):
            for col in range(cols):
                positions[mat[row][col]] = (row, col)

        for i, n in enumerate(arr):
            row, col = positions[n]

            row_count[row] += 1
            col_count[col] += 1

            if row_count[row] == cols or col_count[col] == rows:
                return i

        return -1


# @lc code=end
