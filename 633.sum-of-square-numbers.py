#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_b = int(math.sqrt(c))

        for b in range(max_b, -1, -1):
            remainder = c - b * b
            a = math.sqrt(remainder)
            if a == int(a):
                return True

        return False


# @lc code=end
