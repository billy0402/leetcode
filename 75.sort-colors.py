#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """Return None.

        Do not return anything, modify nums in-place instead.
        """

        def swap(i: int, j: int):
            nums[i], nums[j] = nums[j], nums[i]

        l, i, r = 0, 0, len(nums) - 1
        while i <= r:
            if nums[i] == 0:
                swap(l, i)
                l += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1


# @lc code=end
