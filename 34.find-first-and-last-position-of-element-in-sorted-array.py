#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import Union


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def find_index(kind: Union['first', 'last']):
            left = 0
            right = len(nums) - 1
            index = -1
            while left <= right:
                middle = (left + right) // 2
                n = nums[middle]
                if n < target:
                    left = middle + 1
                elif n > target:
                    right = middle - 1
                else:
                    index = middle
                    if kind == 'first':
                        right = middle - 1
                    elif kind == 'last':
                        left = middle + 1
            return index

        first = find_index('first')
        last = find_index('last')
        return [first, last]


# @lc code=end
