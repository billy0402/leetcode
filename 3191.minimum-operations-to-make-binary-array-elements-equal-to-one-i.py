#
# @lc app=leetcode id=3191 lang=python3
#
# [3191] Minimum Operations to Make Binary Array Elements Equal to One I
#

# @lc code=start
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        counter = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                nums[i] = 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
                counter += 1

        if nums[-2] == 0 or nums[-1] == 0:
            return -1
        return counter


# @lc code=end
