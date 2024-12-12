#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

# @lc code=start
import heapq

CAN_COMPARE = 2


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) >= CAN_COMPARE:
            largest = -heapq.heappop(stones)
            secondary = -heapq.heappop(stones)

            if largest != secondary:
                heapq.heappush(stones, -(largest - secondary))

        return -stones[0] if stones else 0


# @lc code=end
