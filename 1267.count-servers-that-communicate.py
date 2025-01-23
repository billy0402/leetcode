#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#

# @lc code=start
class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        row_servers = [0] * rows
        col_servers = [0] * cols
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    row_servers[row] += 1
                    col_servers[col] += 1

        counter = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and max(row_servers[row], col_servers[col]) > 1:
                    counter += 1
        return counter


# @lc code=end
