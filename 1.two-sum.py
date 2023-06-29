#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n1 in enumerate(nums):
            n2 = target - n1

            try:
                j = nums.index(n2, i + 1)
                return [i, j]
            except ValueError:
                continue

        return []


# @lc code=end
