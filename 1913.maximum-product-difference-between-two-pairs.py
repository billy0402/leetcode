#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        min1, min2, *_, max2, max1 = nums
        return (max1 * max2) - (min1 * min2)


# @lc code=end
