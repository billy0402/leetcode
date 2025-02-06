#
# @lc app=leetcode id=1752 lang=python3
#
# [1752] Check if Array Is Sorted and Rotated
#

# @lc code=start
class Solution:
    def check(self, nums: list[int]) -> bool:
        counter = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                counter += 1
        return counter == 0 or (counter == 1 and nums[-1] <= nums[0])


# @lc code=end
