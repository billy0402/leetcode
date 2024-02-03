#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#


# @lc code=start
class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        removed_once = False

        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                if removed_once:
                    return False

                if i >= 2 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]

                removed_once = True

        return True


# @lc code=end
