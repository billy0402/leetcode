#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#


# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1

        for i in range(1, n + 1):
            one_digit = int(s[i - 1])
            if one_digit != 0:
                dp[i] += dp[i - 1]

            if i < 2:
                continue

            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]


# @lc code=end
