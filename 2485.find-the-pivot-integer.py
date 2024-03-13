#
# @lc app=leetcode id=2485 lang=python3
#
# [2485] Find the Pivot Integer
#

# @lc code=start
import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        total = (1 + n) * n // 2
        pivot = int(math.sqrt(total))
        return pivot if pivot * pivot == total else -1


# @lc code=end
