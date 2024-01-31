#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#


# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        results: list[int] = [-1] * len(nums)
        stack: list[int] = []

        for _ in range(2):
            for i in range(len(nums)):
                n = nums[i]
                while stack and n > nums[stack[-1]]:
                    top = stack.pop()
                    results[top] = n

                stack.append(i)

        return results


# @lc code=end
