#
# @lc app=leetcode id=3330 lang=python3
#
# [3330] Find the Original Typed String I
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        return 1 + sum([1 for i in range(1, len(word)) if word[i] == word[i - 1]])


# @lc code=end
