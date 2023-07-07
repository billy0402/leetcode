#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#


# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, x + 1):
            if i * i > x:
                return i - 1

        return x


# @lc code=end
