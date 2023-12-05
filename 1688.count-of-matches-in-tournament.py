#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#


# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n >= 2:
            if n % 2 != 0:
                matches += (n - 1) // 2 + 1
            else:
                matches += n // 2

            n //= 2

        return matches


# @lc code=end
