#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#


# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        s = str(bin(n)).replace('0', '')
        return len(s) - 1


# @lc code=end
