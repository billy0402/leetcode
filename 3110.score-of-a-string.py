#
# @lc app=leetcode id=3110 lang=python3
#
# [3110] Score of a String
#

# @lc code=start
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score


# @lc code=end
