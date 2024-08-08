#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        rows, cols = n, n
        r, c = 0, -1
        direction = 1  # 1 or -1
        result: list[list[int]] = [([0] * cols) for _ in range(rows)]
        i = 1

        while rows and cols:
            for _ in range(cols):
                # 1 is right, -1 is left
                c += direction
                result[r][c] = i
                i += 1
            rows -= 1

            for _ in range(rows):
                # 1 is bottom, -1 is top
                r += direction
                result[r][c] = i
                i += 1
            cols -= 1

            direction *= -1

        return result


# @lc code=end
