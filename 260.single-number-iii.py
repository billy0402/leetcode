#
# @lc app=leetcode id=260 lang=python3
#
# [260] Single Number III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor = 0
        for n in nums:
            xor ^= n

        # find the rightmost bit
        mask = xor & -xor

        num1 = 0
        for n in nums:
            if n & mask:
                num1 ^= n

        return [num1, num1 ^ xor]


# @lc code=end
