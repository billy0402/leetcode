#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtracking(start: int, current_sum: int):
            if current_sum == target:
                answers.append(current.copy())
                return

            for i in range(start, n):
                num = candidates[i]

                if i > start and num == candidates[i - 1]:
                    continue

                if current_sum + num > target:
                    break

                current.append(num)
                backtracking(i + 1, current_sum + num)
                current.pop()

        answers: list[list[int]] = []
        current: list[int] = []
        candidates.sort()
        n = len(candidates)
        backtracking(0, 0)
        return answers


# @lc code=end
