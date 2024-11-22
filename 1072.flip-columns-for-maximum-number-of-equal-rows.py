#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#

# @lc code=start
from collections import defaultdict


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        pattern_frequencies: dict[str, int] = defaultdict(int)

        for row in matrix:
            row_pattern = "".join("T" if n == row[0] else "F" for n in row)
            pattern_frequencies[row_pattern] += 1

        return max(pattern_frequencies.values())


# @lc code=end
