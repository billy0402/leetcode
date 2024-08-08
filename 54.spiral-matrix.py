#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, -1
        direction = 1  # 1 or -1
        result: list[int] = []

        while rows and cols:
            for _ in range(cols):
                # 1 is right, -1 is left
                c += direction
                result.append(matrix[r][c])
            rows -= 1

            for _ in range(rows):
                # 1 is bottom, -1 is top
                r += direction
                result.append(matrix[r][c])
            cols -= 1

            direction *= -1

        return result


# @lc code=end
