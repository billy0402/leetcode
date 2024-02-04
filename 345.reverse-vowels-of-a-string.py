#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        left, right = 0, len(letters) - 1
        vowels = {'a', 'e', 'i', 'o', 'u'}

        while left < right:
            if letters[left].lower() not in vowels:
                left += 1
                continue

            if letters[right].lower() not in vowels:
                right -= 1
                continue

            letters[left], letters[right] = letters[right], letters[left]
            left += 1
            right -= 1

        return ''.join(letters)


# @lc code=end
