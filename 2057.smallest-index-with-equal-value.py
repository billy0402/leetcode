#
# @lc app=leetcode id=2057 lang=python3
#
# [2057] Smallest Index With Equal Value
#


# @lc code=start
class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        for i, n in enumerate(nums):
            if i % 10 == n:
                return i
        return -1


# @lc code=end
