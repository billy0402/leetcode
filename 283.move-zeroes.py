#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        counter = 0
        length = len(nums)

        for i in range(length):
            n = nums[i]
            if n != 0:
                nums[counter] = n
                counter += 1

        for i in range(counter, length):
            nums[i] = 0


# @lc code=end
