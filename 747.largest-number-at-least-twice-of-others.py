#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#

# @lc code=start
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)

        for num in nums:
            if num == max_num:
                continue

            if num * 2 > max_num:
                return -1

        return nums.index(max_num)


# @lc code=end
