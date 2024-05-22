#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtracking(i: int, current: list[str]):
            if i == len(s):
                answers.append(current.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    current.append(s[i : j + 1])
                    backtracking(j + 1, current)
                    current.pop()

        answers: list[list[str]] = []
        backtracking(0, [])
        return answers


# @lc code=end
