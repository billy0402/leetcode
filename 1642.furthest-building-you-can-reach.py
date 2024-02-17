#
# @lc app=leetcode id=1642 lang=python3
#
# [1642] Furthest Building You Can Reach
#

# @lc code=start
import heapq


class Solution:
    def furthestBuilding(
        self,
        heights: list[int],
        bricks: int,
        ladders: int,
    ) -> int:
        n = len(heights)
        climbs: list[int] = []

        for i in range(1, n):
            building1 = heights[i - 1]
            building2 = heights[i]
            height = building2 - building1
            if height <= 0:
                continue

            heapq.heappush(climbs, height)

            if len(climbs) > ladders:
                bricks -= heapq.heappop(climbs)

            if bricks < 0:
                return i - 1

        return n - 1


# @lc code=end
