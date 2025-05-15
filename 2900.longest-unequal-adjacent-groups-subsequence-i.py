#
# @lc app=leetcode id=2900 lang=python3
#
# [2900] Longest Unequal Adjacent Groups Subsequence I
#

# @lc code=start
class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        return [words[0]] + [
            words[i] for i in range(1, len(groups)) if groups[i] != groups[i - 1]
        ]


# @lc code=end
