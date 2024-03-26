#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#


# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] < 0:
                nums[i] = 0

        for n in nums:
            n = abs(n)
            if n < 1 or n > length:
                continue

            mark = nums[n - 1]
            if mark > 0:
                nums[n - 1] *= -1
            elif mark == 0:
                nums[n - 1] = -(length + 1)

        for i in range(1, length + 1):
            if nums[i - 1] >= 0:
                return i

        return length + 1


# @lc code=end
