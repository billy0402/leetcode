#
# @lc app=leetcode id=1561 lang=python3
#
# [1561] Maximum Number of Coins You Can Get
#

# @lc code=start
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)

        sum = 0
        for i in range(1, len(piles) // 3 * 2, 2):
            sum += piles[i]

        return sum


# @lc code=end
