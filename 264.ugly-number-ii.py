#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#


# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        a = b = c = 0

        for i in range(1, n):
            dp[i] = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)

            if dp[a] * 2 == dp[i]:
                a += 1
            if dp[b] * 3 == dp[i]:
                b += 1
            if dp[c] * 5 == dp[i]:
                c += 1

        return dp[n - 1]


# @lc code=end
