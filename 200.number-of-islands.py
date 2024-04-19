#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#


# @lc code=start
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(x: int, y: int):
            if not 0 <= x < ROW or not 0 <= y < COLUMN or grid[x][y] != ISLAND:
                return

            grid[x][y] = WATER  # mark as visited
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        islands = 0
        ROW, COLUMN = len(grid), len(grid[0])
        WATER, ISLAND = '0', '1'

        for x in range(ROW):
            for y in range(COLUMN):
                if grid[x][y] == ISLAND:
                    islands += 1
                    dfs(x, y)

        return islands


# @lc code=end
