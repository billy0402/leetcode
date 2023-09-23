#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 10:
                break

            digits[i] -= 10
            if i == 0:
                digits.insert(0, 1)
            else:
                digits[i - 1] += 1

        return digits


# @lc code=end
