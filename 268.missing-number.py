#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        xor = 0
        for i, n in enumerate(nums):
            xor ^= (i + 1) ^ n
        return xor


# @lc code=end
