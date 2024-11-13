#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#

# @lc code=start
from bisect import bisect_left, bisect_right


class Solution:
    def countFairPairs(self, nums: list[int], lower: int, upper: int) -> int:
        nums.sort()

        pairs = 0
        for i, n in enumerate(nums):
            left = bisect_left(nums, lower - n, i + 1)
            right = bisect_right(nums, upper - n, i + 1)
            pairs += right - left
        return pairs


# @lc code=end
