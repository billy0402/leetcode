#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#


# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answers: list[int] = [0] * n
        left = 0
        right = n - 1

        for i in range(n - 1, -1, -1):
            if abs(nums[left]) >= abs(nums[right]):
                answers[i] = nums[left]**2
                left += 1
            else:
                answers[i] = nums[right]**2
                right -= 1

        return answers


# @lc code=end
