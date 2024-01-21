#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#


# @lc code=start
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtracking(visited: set[int], current: list[int]):
            if len(current) == len(nums):
                answers.append(current.copy())
                return

            for n in nums:
                if n not in visited:
                    visited.add(n)
                    current.append(n)
                    backtracking(visited, current)
                    visited.remove(n)
                    current.pop()

        answers = []
        backtracking(set(), [])
        return answers


# @lc code=end
