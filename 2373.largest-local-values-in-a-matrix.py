#
# @lc app=leetcode id=2373 lang=python3
#
# [2373] Largest Local Values in a Matrix
#


# @lc code=start
class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        def find_sub_matrix_max(center_x: int, center_y: int):
            matrix_max = 0
            for x in range(center_x - 1, center_x + 2):
                for y in range(center_y - 1, center_y + 2):
                    matrix_max = max(matrix_max, grid[x][y])
            return matrix_max

        N = len(grid) - 1
        answer: list[list[int]] = []

        for x in range(1, N):
            row: list[int] = []

            for y in range(1, N):
                sub_matrix_max = find_sub_matrix_max(x, y)
                row.append(sub_matrix_max)

            answer.append(row)

        return answer


# @lc code=end
