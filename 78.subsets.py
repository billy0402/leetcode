#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#


# @lc code=start
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtracking(start_index: int, current: list[int]):
            answers.append(current.copy())

            for i in range(start_index, len(nums)):
                current.append(nums[i])
                backtracking(i + 1, current)
                current.pop()

        answers = []
        backtracking(0, [])
        return answers


# @lc code=end
