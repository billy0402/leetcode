#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        excepted = (1 + n) * n // 2
        return excepted - sum(nums)


# @lc code=end
