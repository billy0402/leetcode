#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
import math
from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for n in nums:
            cache[n] += 1

        counter = 0
        for value in cache.values():
            if value == 1:
                return -1

            counter += math.ceil(value / 3)

        return counter


# @lc code=end
