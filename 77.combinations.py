#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtracking(start_index: int, comb: list[int]):
            if len(comb) + (len(nums) - start_index) < k:
                return

            if len(comb) == k:
                answers.append(comb.copy())
                return comb

            for i in range(start_index, n):
                comb.append(nums[i])
                backtracking(i + 1, comb)
                comb.pop()

        answers = []
        nums = list(range(1, n + 1))
        backtracking(0, [])
        return answers


# @lc code=end
