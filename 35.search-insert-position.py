#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            n = nums[middle]
            if n == target:
                return middle
            elif n > target:
                right = middle - 1
            else:
                left = middle + 1
        return left


# @lc code=end
