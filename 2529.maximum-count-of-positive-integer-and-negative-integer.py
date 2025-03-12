#
# @lc app=leetcode id=2529 lang=python3
#
# [2529] Maximum Count of Positive Integer and Negative Integer
#

# @lc code=start
class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        pos = len(nums) - self._upper_bound(nums)
        neg = self._lower_bound(nums) + 1
        return max(pos, neg)

    def _upper_bound(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] > 0:
                right = middle - 1  # move left
            else:
                left = middle + 1  # move right
        return left  # the first positive number

    def _lower_bound(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < 0:
                left = middle + 1  # move right
            else:
                right = middle - 1  # move left
        return right  # the last negative number


# @lc code=end
