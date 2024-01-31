#
# @lc app=leetcode id=2129 lang=python3
#
# [2129] Capitalize the Title
#


# @lc code=start
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split(' ')
        words = [word.capitalize() if len(word) > 2 else word for word in words]
        return ' '.join(words)


# @lc code=end
