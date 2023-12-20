#
# @lc app=leetcode id=2706 lang=python3
#
# [2706] Buy Two Chocolates
#

# @lc code=start
from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        min1, min2, *_ = prices

        balance = money - min1 - min2
        return balance if balance >= 0 else money


# @lc code=end
