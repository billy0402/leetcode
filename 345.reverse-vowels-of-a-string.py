#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        letters: list[str] = []
        vowels: list[str] = []

        for char in s:
            if char in 'aeiouAEIOU':
                letters.append('*')
                vowels.append(char)
            else:
                letters.append(char)

        for i in range(len(letters)):
            char = letters[i]
            if char == '*':
                letters[i] = vowels.pop()

        return ''.join(letters)


# @lc code=end
