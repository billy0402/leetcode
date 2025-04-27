#
# @lc app=leetcode id=3392 lang=python3
#
# [3392] Count Subarrays of Length Three With a Condition
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int]) -> int:
        counter = 0

        for i in range(len(nums) - 2):
            first, second, third = nums[i], nums[i + 1], nums[i + 2]
            if (first + third) * 2 == second:
                counter += 1

        return counter


# @lc code=end
