#
# @lc app=leetcode id=885 lang=python3
#
# [885] Spiral Matrix III
#

# @lc code=start
class Solution:
    def spiralMatrixIII(
        self,
        rows: int,
        cols: int,
        r_start: int,
        c_start: int,
    ) -> list[list[int]]:
        result = [[r_start, c_start]]
        r, c = r_start, c_start
        direction = 1  # 1 or -1
        steps = 1

        while len(result) < rows * cols:
            for _ in range(steps):
                # 1 is right, -1 is left
                c += direction
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

            for _ in range(steps):
                # 1 is bottom, -1 is top
                r += direction
                if 0 <= r < rows and 0 <= c < cols:
                    result.append([r, c])

            direction *= -1
            steps += 1

        return result


# @lc code=end
