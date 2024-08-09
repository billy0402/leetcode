#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#

# @lc code=start
class Solution:
    def numMagicSquaresInside(self, grid: list[list[int]]) -> int:
        def is_magic_square(r: int, c: int) -> bool:
            seen: set[int] = set()
            for x in range(r, r + 3):
                for y in range(c, c + 3):
                    n = grid[x][y]
                    if not (1 <= n <= 9) or n in seen:
                        return False
                    seen.add(n)

            diagonal1 = grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2]
            diagonal2 = grid[r + 2][c] + grid[r + 1][c + 1] + grid[r][c + 2]
            if diagonal1 != 15 or diagonal2 != 15:
                return False

            row1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
            row2 = grid[r + 1][c] + grid[r + 1][c + 1] + grid[r + 1][c + 2]
            row3 = grid[r + 2][c] + grid[r + 2][c + 1] + grid[r + 2][c + 2]
            if row1 != 15 or row2 != 15 or row3 != 15:
                return False

            col1 = grid[r][c] + grid[r][c + 1] + grid[r][c + 2]
            col2 = grid[r][c + 1] + grid[r + 1][c + 1] + grid[r + 2][c + 1]
            col3 = grid[r][c + 2] + grid[r + 1][c + 2] + grid[r + 2][c + 2]
            if col1 != 15 or col2 != 15 or col3 != 15:
                return False

            return True

        rows, cols = len(grid), len(grid[0])
        counter = 0
        for r in range(rows - 2):
            for c in range(cols - 2):
                if is_magic_square(r, c):
                    counter += 1
        return counter


# @lc code=end
