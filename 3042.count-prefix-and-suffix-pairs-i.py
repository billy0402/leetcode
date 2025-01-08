#
# @lc app=leetcode id=3042 lang=python3
#
# [3042] Count Prefix and Suffix Pairs I
#

# @lc code=start
class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        n = len(words)
        counter = 0

        for i in range(n):
            for j in range(i + 1, n):
                s1 = words[i]
                s2 = words[j]

                if len(s1) > len(s2):
                    continue

                if s2.startswith(s1) and s2.endswith(s1):
                    counter += 1

        return counter


# @lc code=end
