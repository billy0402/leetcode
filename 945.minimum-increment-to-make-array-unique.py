#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()

        counter = 0

        for i in range(1, len(nums)):
            p, c = nums[i - 1], nums[i]

            if c <= p:
                counter += p - c + 1
                nums[i] = p + 1

        return counter


# @lc code=end
