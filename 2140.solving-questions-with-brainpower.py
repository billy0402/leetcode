#
# @lc app=leetcode id=2140 lang=python3
#
# [2140] Solving Questions With Brainpower
#

# @lc code=start
class Solution:
    def mostPoints(self, questions: list[list[int]]) -> int:
        cache = [0] * len(questions)

        def backtracking(i: int) -> int:
            if i >= len(questions):
                return 0

            if cache[i]:
                return cache[i]

            points, brainpower = questions[i]
            cache[i] = max(
                backtracking(i + 1),  # skip
                points + backtracking(i + 1 + brainpower),  # solve
            )
            return cache[i]

        return backtracking(0)


# @lc code=end
