#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#


# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets: dict[str, int] = {}

        for char in s:
            alphabets[char] = alphabets.get(char, 0) + 1

        for key, value in alphabets.items():
            if value == 1:
                return s.index(key)

        return -1


# @lc code=end
