#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#


# @lc code=start
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        results: list[int] = [1] * len(nums)
        prefix_product = 1
        suffix_product = 1

        for i in range(len(nums)):
            n = nums[i]
            results[i] *= prefix_product
            prefix_product *= n

        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            results[i] *= suffix_product
            suffix_product *= n

        return results


# @lc code=end
