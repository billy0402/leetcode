#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        current, previous = 0, 0
        for n in nums:
            current, previous = previous, current
            current = max(current + n, previous)
        return current


# @lc code=end
