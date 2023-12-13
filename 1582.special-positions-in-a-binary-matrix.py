#
# @lc app=leetcode id=1582 lang=python3
#
# [1582] Special Positions in a Binary Matrix
#

# @lc code=start
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        results = 0

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    continue

                row = sum(mat[i])
                col = sum([row[j] for row in mat])
                if row == 1 and col == 1:
                    results += 1

        return results


# @lc code=end
