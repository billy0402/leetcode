#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#

# @lc code=start
mod = 10**9 + 7


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        def dice(n: int, k: int, target: int) -> int:
            if n == 0 and target == 0:
                return 1
            if n == 0 or target <= 0:
                return 0

            if dp[n][target] != -1:
                return dp[n][target] % mod

            ways = 0
            for i in range(1, k + 1):
                ways += dice(n - 1, k, target - i)
            dp[n][target] = ways
            return dp[n][target] % mod

        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        dice(n, k, target)
        return dp[n][target] % mod


# @lc code=end
