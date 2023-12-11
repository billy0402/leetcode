#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cache = {}

        for num in arr:
            cache[num] = cache.get(num, 0) + 1

            if cache[num] > len(arr) // 4:
                return num


# @lc code=end
