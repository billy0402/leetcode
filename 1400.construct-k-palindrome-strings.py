#
# @lc app=leetcode id=1400 lang=python3
#
# [1400] Construct K Palindrome Strings
#

# @lc code=start
from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        if len(s) == k:
            return True

        counter = Counter(s)
        odd_count = sum(count % 2 for count in counter.values())

        return odd_count <= k


# @lc code=end
