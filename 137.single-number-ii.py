#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones ^= num & ~twos
            twos ^= num & ~ones

        return ones


# @lc code=end
