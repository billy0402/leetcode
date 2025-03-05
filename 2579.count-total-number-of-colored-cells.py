#
# @lc app=leetcode id=2579 lang=python3
#
# [2579] Count Total Number of Colored Cells
#

# @lc code=start
class Solution:
    def coloredCells(self, n: int) -> int:
        """Mathematical formula.

        1 + (4x1) + (4x2) + ... + (4x(n-1))
        = 1 + 4 x (((n - 1) x n) / 2)
        = 1 + 2 x (n - 1) x n
        """

        return 1 + 2 * (n - 1) * n


# @lc code=end
