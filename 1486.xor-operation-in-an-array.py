#
# @lc app=leetcode id=1486 lang=python3
#
# [1486] XOR Operation in an Array
#


# @lc code=start
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0
        for i in range(start, start + 2 * n, 2):
            xor ^= i
        return xor


# @lc code=end
