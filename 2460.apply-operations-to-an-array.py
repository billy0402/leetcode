#
# @lc app=leetcode id=2460 lang=python3
#
# [2460] Apply Operations to an Array
#

# @lc code=start
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        l = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        return nums


# @lc code=end
