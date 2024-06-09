#
# @lc app=leetcode id=560 lang=python3
#
# [560] Subarray Sum Equals K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counter = 0
        current_sum = 0
        prefix_sums: dict[int, int] = defaultdict(int, {0: 1})

        for n in nums:
            current_sum += n
            diff = current_sum - k

            counter += prefix_sums[diff]
            prefix_sums[current_sum] += 1

        return counter


# @lc code=end
