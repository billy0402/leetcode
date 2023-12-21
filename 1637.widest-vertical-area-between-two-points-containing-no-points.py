#
# @lc app=leetcode id=1637 lang=python3
#
# [1637] Widest Vertical Area Between Two Points Containing No Points
#

# @lc code=start
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])

        max_width = 0
        for i in range(len(points) - 1):
            px, py = points[i]
            qx, qy = points[i + 1]
            if qx - px > max_width:
                max_width = qx - px

        return max_width


# @lc code=end
