#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
#


# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        score: int = float("-inf")  # pyright:ignore[reportAssignmentType]
        zeros = 0
        ones = 0

        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros += 1
            elif s[i] == "1":
                ones += 1
            score = max(score, zeros - ones)  # left use ones

        if s[-1] == "1":
            ones += 1

        return score + ones


# @lc code=end
