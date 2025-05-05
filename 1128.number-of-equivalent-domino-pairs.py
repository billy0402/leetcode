#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#

# @lc code=start
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: list[list[int]]) -> int:
        counter = 0
        pairs: dict[tuple[int, int], int] = defaultdict(int)

        for a, b in dominoes:
            a, b = min(a, b), max(a, b)
            counter += pairs[a, b]
            pairs[a, b] += 1

        return counter


# @lc code=end
