#
# @lc app=leetcode id=3066 lang=python3
#
# [3066] Minimum Operations to Exceed Threshold Value II
#

# @lc code=start
import heapq


class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        counter = 0

        heapq.heapify(nums)

        while nums[0] < k:
            min1 = heapq.heappop(nums)
            min2 = heapq.heappop(nums)
            new_value = min1 * 2 + min2
            heapq.heappush(nums, new_value)
            counter += 1

        return counter


# @lc code=end
