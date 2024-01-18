#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        for i in range(n - 1):
            a, b = b, a + b
        return a


# @lc code=end
