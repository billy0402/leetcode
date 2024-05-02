#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#


# @lc code=start
class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        seen: set[int] = set()
        max_positive = -1

        for n in nums:
            if -n in seen:
                max_positive = max(max_positive, abs(n))

            seen.add(n)

        return max_positive


# @lc code=end
