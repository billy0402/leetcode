#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#


# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        results = ''
        length = max(len(word1), len(word2))

        for i in range(length):
            if len(word1) > i:
                results += word1[i]

            if len(word2) > i:
                results += word2[i]

        return results


# @lc code=end
