#
# @lc app=leetcode id=2942 lang=python3
#
# [2942] Find Words Containing Character
#

# @lc code=start
class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, w in enumerate(words) if x in w]


# @lc code=end
