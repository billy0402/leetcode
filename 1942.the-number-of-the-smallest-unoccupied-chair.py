#
# @lc app=leetcode id=1942 lang=python3
#
# [1942] The Number of the Smallest Unoccupied Chair
#

# @lc code=start
import heapq


class Solution:
    def smallestChair(self, times: list[list[int]], target_friend: int) -> int:
        indexes = list(range(len(times)))
        indexes.sort(key=lambda i: times[i][0])

        available_chairs = list(range(len(times)))
        used_chairs: list[tuple[int, int]] = []  # (leaving, chair)

        for i in indexes:
            arrival, leaving = times[i]

            while used_chairs and used_chairs[0][0] <= arrival:
                _, chair = heapq.heappop(used_chairs)
                heapq.heappush(available_chairs, chair)

            chair = heapq.heappop(available_chairs)
            if i == target_friend:
                return chair

            heapq.heappush(used_chairs, (leaving, chair))

        return -1


# @lc code=end
