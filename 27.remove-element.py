#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[counter] = nums[i]
                counter += 1
        return counter


# @lc code=end
