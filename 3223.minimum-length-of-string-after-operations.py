#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        counter = Counter(s)
        removed = 0

        for frequency in counter.values():
            if frequency % 2:
                removed += frequency - 1
            else:
                removed += frequency - 2

        return len(s) - removed


# @lc code=end
