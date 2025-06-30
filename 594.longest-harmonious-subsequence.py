#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#

# @lc code=start
from collections import Counter


class Solution:
    def findLHS(self, nums: list[int]) -> int:
        max_length = 0
        counter = Counter(nums)

        for n in counter:
            if n + 1 in counter:
                max_length = max(max_length, counter[n] + counter[n + 1])

        return max_length


# @lc code=end
