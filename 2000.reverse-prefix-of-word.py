#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#


# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix: list[str] = []

        for i, char in enumerate(word):
            prefix.append(char)

            if char == ch:
                return ''.join(reversed(prefix)) + word[i + 1:]

        return word


# @lc code=end
