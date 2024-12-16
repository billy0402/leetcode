#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
import heapq


class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        heap = [(n, i) for (i, n) in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            _, i = heapq.heappop(heap)
            nums[i] *= multiplier
            heapq.heappush(heap, (nums[i], i))

        return nums


# @lc code=end
