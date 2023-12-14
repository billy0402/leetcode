#
# @lc app=leetcode id=2482 lang=python3
#
# [2482] Difference Between Ones and Zeros in Row and Column
#

# @lc code=start
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = []
        row_length = len(grid[0])
        col_length = len(grid)
        row_ones = [sum([n for n in grid[y]]) for y in range(col_length)]
        col_ones = [sum([col[x] for col in grid]) for x in range(row_length)]

        for y in range(col_length):
            for x in range(row_length):
                results = row_ones[y] + col_ones[x] \
                    - (row_length - row_ones[y]) \
                    - (col_length - col_ones[x])

                if len(diff) <= y:
                    diff.append([])
                diff[y].append(results)

        return diff


# @lc code=end
