#
# @lc app=leetcode id=2558 lang=python3
#
# [2558] Take Gifts From the Richest Pile
#

# @lc code=start
import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            largest = -heapq.heappop(gifts)
            heapq.heappush(gifts, -int(math.sqrt(largest)))

        return -sum(gifts)


# @lc code=end
