#
# @lc app=leetcode id=1992 lang=python3
#
# [1992] Find All Groups of Farmland
#


# @lc code=start
class Solution:
    def findFarmland(self, land: list[list[int]]) -> list[list[int]]:
        def dfs(x: int, y: int, farm: list[int]):
            if not 0 <= x < ROW or not 0 <= y < COLUMN or land[x][y] != FARM:
                return

            land[x][y] = 0  # mark as visited

            farm[0] = min(farm[0], x)
            farm[1] = min(farm[1], y)
            farm[2] = max(farm[2], x)
            farm[3] = max(farm[3], y)

            dfs(x - 1, y, farm)
            dfs(x + 1, y, farm)
            dfs(x, y - 1, farm)
            dfs(x, y + 1, farm)

        answers: list[list[int]] = []
        ROW, COLUMN = len(land), len(land[0])
        FOREST, FARM = 0, 1

        for x in range(ROW):
            for y in range(COLUMN):
                if land[x][y] == FARM:
                    farm = [x, y, x, y]
                    dfs(x, y, farm)
                    answers.append(farm)

        return answers


# @lc code=end
