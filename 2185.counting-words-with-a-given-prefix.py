#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start


class Solution:
    def prefixCount(self, words: list[str], prefix: str) -> int:
        return sum(word.startswith(prefix) for word in words)


# @lc code=end
