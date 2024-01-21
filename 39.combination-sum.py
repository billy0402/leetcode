#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#


# @lc code=start
class Solution:
    def combinationSum(self, candidates: list[int], target: int) \
      -> list[list[int]]:
        def backtracking(current: list[int]):
            if sum(current) > target:
                return

            if sum(current) == target:
                copy = sorted(current)
                if copy not in answers:
                    answers.append(copy)
                return

            for n in candidates:
                current.append(n)
                backtracking(current)
                current.pop()

        answers = []
        backtracking([])
        return answers


# @lc code=end
