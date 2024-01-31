#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#


# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        xs, ys = x1 - x0, y1 - y0

        for x, y in coordinates:
            # (y - y1) / (x - x1) = (y1 - y0) / (x1 - x0) -> ZeroDivisionError
            # (y - y1) * (x1 - x0) = (y1 - y0) * (x - x1)
            if (y - y1) * xs != ys * (x - x1):
                return False

        return True


# @lc code=end
