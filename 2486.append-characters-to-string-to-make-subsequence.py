#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        si = ti = 0

        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                ti += 1
            si += 1

        return len(t) - ti


# @lc code=end
