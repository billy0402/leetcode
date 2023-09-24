#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#


# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''.join(letter.lower() for letter in s if letter.isalnum())

        middle = len(clean) // 2

        if len(clean) % 2 == 0:
            return clean[:middle] == clean[:middle - 1:-1]
        return clean[:middle] == clean[:middle:-1]


# @lc code=end
