#
# @lc app=leetcode id=3000 lang=python3
#
# [3000] Maximum Area of Longest Diagonal Rectangle
#

# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        max_squared_diagonal = 0
        max_area = 0

        for x, y in dimensions:
            squared_diagonal = x * x + y * y
            area = x * y
            if squared_diagonal > max_squared_diagonal:
                max_squared_diagonal = max(max_squared_diagonal, squared_diagonal)
                max_area = area
            elif squared_diagonal == max_squared_diagonal:
                max_area = max(max_area, area)

        return max_area


# @lc code=end
