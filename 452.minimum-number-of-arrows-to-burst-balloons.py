#
# @lc app=leetcode id=452 lang=python3
#
# [452] Minimum Number of Arrows to Burst Balloons
#


# @lc code=start
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[0])
        arrow_end = float('-inf')
        arrows = 0

        for start, end in points:
            if start > arrow_end:
                arrow_end = end
                arrows += 1
            else:
                arrow_end = min(arrow_end, end)

        return arrows


# @lc code=end
