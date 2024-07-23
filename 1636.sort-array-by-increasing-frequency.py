#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from collections import Counter


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        frequencies = Counter(nums)
        return sorted(nums, key=lambda x: (frequencies[x], -x))


# @lc code=end
