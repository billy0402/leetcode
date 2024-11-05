#
# @lc app=leetcode id=2914 lang=python3
#
# [2914] Minimum Number of Changes to Make Binary String Beautiful
#

# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:
        counter = 0
        for i in range(0, len(s), 2):
            if s[i] != s[i + 1]:
                counter += 1
        return counter


# @lc code=end
