#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        prefix = ''
        for i in range(0, len(shortest)):
            prefix += shortest[i]
            isPrefix = all(text.startswith(prefix) for text in strs)
            if not isPrefix:
                prefix = prefix[:-1]
                break

        return prefix


# @lc code=end
