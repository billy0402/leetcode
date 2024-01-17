#
# @lc app=leetcode id=1207 lang=python3
#
# [1207] Unique Number of Occurrences
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        digits = defaultdict(int)
        for n in arr:
            digits[n] += 1

        return len(digits.keys()) == len(set(digits.values()))


# @lc code=end
