#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
from typing import List

max_size = 2**31 - 1
min_size = -2**31


class Solution:
    def reverse(self, x: int) -> int:
        positive_x = abs(x)

        l: List[str] = []
        for num in str(positive_x):
            l.insert(0, str(num))

        reverse_x = ''.join(l)
        multiplier = -1 if x != positive_x else 1
        result = int(reverse_x) * multiplier

        if result >= max_size or result <= min_size:
            return 0
        return result


# @lc code=end
