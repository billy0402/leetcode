#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        counter = 0
        current_sum = 0
        prefix_remainders: dict[int, int] = defaultdict(int, {0: 1})

        for n in nums:
            current_sum += n
            remainder = current_sum % k

            counter += prefix_remainders[remainder]
            prefix_remainders[remainder] += 1

        return counter


# @lc code=end
