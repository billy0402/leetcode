#
# @lc app=leetcode id=214 lang=python3
#
# [214] Shortest Palindrome
#

# @lc code=start
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        pointer = 0
        for i in range(len(s) - 1, -1, -1):
            if s[pointer] == s[i]:
                pointer += 1

        if pointer == len(s):
            return s

        non_palindrome = s[pointer:]
        return (
            non_palindrome[::-1] + self.shortestPalindrome(s[:pointer]) + non_palindrome
        )


# @lc code=end
