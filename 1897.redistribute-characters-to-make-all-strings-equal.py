#
# @lc app=leetcode id=1897 lang=python3
#
# [1897] Redistribute Characters to Make All Strings Equal
#

# @lc code=start
from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        cache = defaultdict(int)

        for word in words:
            for char in word:
                cache[char] += 1

        for value in cache.values():
            if value % len(words) != 0:
                return False

        return True


# @lc code=end
