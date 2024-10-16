#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        return nums[0]


# @lc code=end
