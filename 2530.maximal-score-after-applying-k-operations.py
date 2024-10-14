#
# @lc app=leetcode id=2530 lang=python3
#
# [2530] Maximal Score After Applying K Operations
#

# @lc code=start
import heapq
import math


class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        max_score = 0
        for _ in range(k):
            n = -heapq.heappop(nums)
            max_score += n
            heapq.heappush(nums, -math.ceil(n / 3))
        return max_score


# @lc code=end
