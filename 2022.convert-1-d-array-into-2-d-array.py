#
# @lc app=leetcode id=2022 lang=python3
#
# [2022] Convert 1D Array Into 2D Array
#


# @lc code=start
class Solution:
    def construct2DArray(
        self,
        original: list[int],
        m: int,
        n: int,
    ) -> list[list[int]]:
        if n * m != len(original):
            return []

        results: list[list[int]] = []
        for i in range(m):
            results.append(original[n * i:n * (i + 1)])
        return results


# @lc code=end
