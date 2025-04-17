#
# @lc app=leetcode id=2176 lang=python3
#
# [2176] Count Equal and Divisible Pairs in an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        counter = 0
        prev_indexes: dict[int, set[int]] = defaultdict(set)

        for i, ni in enumerate(nums):
            for j in prev_indexes[ni]:
                if i * j % k == 0:
                    counter += 1
            prev_indexes[ni].add(i)

        return counter


# @lc code=end
