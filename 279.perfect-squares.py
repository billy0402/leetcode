#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
from math import sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        dp[0] = 0

        max_square = int(sqrt(n))
        squares = [i * i for i in range(1, max_square + 1)]

        for target in range(1, n + 1):
            for square in squares:
                if target < square:
                    break
                dp[target] = min(dp[target], dp[target - square] + 1)

        return dp[n]


# @lc code=end
