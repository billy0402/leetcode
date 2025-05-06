#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        for i in range(n):
            nums[i] += nums[nums[i]] % n * n
        for i in range(n):
            nums[i] //= n
        return nums


# @lc code=end
