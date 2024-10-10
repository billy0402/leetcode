#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        n = len(nums)
        stack: list[int] = []

        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(j - stack[-1], max_width)
                stack.pop()
        return max_width


# @lc code=end
