#
# @lc app=leetcode id=2270 lang=python3
#
# [2270] Number of Ways to Split Array
#

# @lc code=start
class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        counter = 0
        left = 0
        right = sum(nums)

        for i in range(len(nums) - 1):
            left += nums[i]
            right -= nums[i]

            if left >= right:
                counter += 1

        return counter


# @lc code=end
