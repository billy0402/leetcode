#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
#

# @lc code=start
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        results = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j >= len(results):
                    results.append([])
                results[j].append(matrix[i][j])

        return results


# @lc code=end
