#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#

# @lc code=start
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()

        positive = nums[-1] * nums[-2] * nums[-3]
        negative = nums[0] * nums[1] * nums[-1]
        return max(positive, negative)


# @lc code=end
