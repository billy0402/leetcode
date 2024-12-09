#
# @lc app=leetcode id=3151 lang=python3
#
# [3151] Special Array I
#

# @lc code=start
class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        return all((nums[i - 1] + nums[i]) % 2 != 0 for i in range(1, len(nums)))


# @lc code=end
