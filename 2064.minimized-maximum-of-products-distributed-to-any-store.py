#
# @lc app=leetcode id=2064 lang=python3
#
# [2064] Minimized Maximum of Products Distributed to Any Store
#

# @lc code=start
import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def can_distribute(x: int) -> bool:
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
                if stores > n:
                    return False
            return True

        min_max = 0
        l, r = 1, max(quantities)
        while l <= r:
            x = (l + r) // 2  # l + (r - l) // 2
            if can_distribute(x):
                min_max = x
                r = x - 1
            else:
                l = x + 1

        return min_max


# @lc code=end
