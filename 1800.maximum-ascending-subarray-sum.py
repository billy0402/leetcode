#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        max_sum = 0
        current_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]

        return max(max_sum, current_sum)


# @lc code=end
