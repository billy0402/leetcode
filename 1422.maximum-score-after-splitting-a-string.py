#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#


# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(len(s) - 1):
            total = 0
            for j in range(i + 1):
                if s[j] == '0':
                    total += 1
            for j in range(i + 1, len(s)):
                if s[j] == '1':
                    total += 1
            result = max(result, total)
        return result


# @lc code=end
