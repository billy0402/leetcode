#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#

# @lc code=start
import heapq


class KthLargest:
    min_heap: list[int]
    k: int

    def __init__(self, k: int, nums: list[int]):
        self.min_heap = nums
        self.k = k

        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)

            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)

        return self.min_heap[0]


# @lc code=end
