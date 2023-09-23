#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        flag = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[flag] = nums[i]
                flag += 1
        return flag


# @lc code=end
