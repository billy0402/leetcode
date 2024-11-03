#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) > len(goal):
            return False
        return s in goal + goal


# @lc code=end
