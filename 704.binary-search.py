#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1


# @lc code=end
