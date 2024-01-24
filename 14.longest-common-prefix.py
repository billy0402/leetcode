#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#


# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]

                if prefix == '':
                    return prefix
        return prefix


# @lc code=end
