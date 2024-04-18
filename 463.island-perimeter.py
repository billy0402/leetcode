#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#


# @lc code=start
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        perimeter = 0
        ROW, COLUMN = len(grid), len(grid[0])
        WATER, ISLAND = 0, 1

        for x in range(ROW):
            for y in range(COLUMN):
                if grid[x][y] == WATER:
                    continue

                island = 4

                if x > 0 and grid[x - 1][y] == ISLAND:
                    island -= 1
                if x < ROW - 1 and grid[x + 1][y] == ISLAND:
                    island -= 1
                if y > 0 and grid[x][y - 1] == ISLAND:
                    island -= 1
                if y < COLUMN - 1 and grid[x][y + 1] == ISLAND:
                    island -= 1

                perimeter += island

        return perimeter


# @lc code=end
