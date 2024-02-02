#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
from typing import Literal


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        direction: Literal['desc', 'asc'] = ''

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:  # equal
                continue

            elif nums[i + 1] > nums[i]:  # asc
                if not direction:
                    direction = 'asc'
                elif direction == 'desc':
                    return False

            else:  # desc
                if not direction:
                    direction = 'desc'
                elif direction == 'asc':
                    return False

        return True


# @lc code=end
