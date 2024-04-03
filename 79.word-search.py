#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#


# @lc code=start
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        def dfs(row: int, col: int, index: int):
            current_point = (row, col)

            if index == len(word):
                return True

            if row < 0 or col < 0 or row >= ROWS or col >= COLS \
               or word[index] != board[row][col] \
               or current_point in visited:
                return False

            visited.add(current_point)
            result = dfs(row + 1, col, index + 1) \
                or dfs(row - 1, col, index + 1) \
                or dfs(row, col + 1, index + 1) \
                or dfs(row, col - 1, index + 1)
            visited.remove(current_point)
            return result

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False


# @lc code=end
