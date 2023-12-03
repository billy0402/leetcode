#
# @lc app=leetcode id=1266 lang=python3
#
# [1266] Minimum Time Visiting All Points
#

# @lc code=start
from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        timer = 0

        for i in range(1, len(points)):
            [s_x, s_y] = points[i - 1]
            [e_x, e_y] = points[i]

            a = abs(e_x - s_x)
            b = abs(e_y - s_y)
            timer += max(a, b)

        return timer


# @lc code=end
