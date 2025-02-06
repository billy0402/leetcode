#
# @lc app=leetcode id=3105 lang=python3
#
# [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
#

# @lc code=start
class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        asc_length = desc_length = max_length = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                asc_length += 1
                desc_length = 1
            elif nums[i] < nums[i - 1]:
                desc_length += 1
                asc_length = 1
            else:
                asc_length = desc_length = 1

            max_length = max(max_length, asc_length, desc_length)

        return max_length


# @lc code=end
