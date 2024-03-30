#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#

# @lc code=start
from collections import defaultdict


class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        return self.slidingWindowAtMost(nums, k) - self.slidingWindowAtMost(
            nums,
            k - 1,
        )

    def slidingWindowAtMost(self, nums: list[int], distinctK: int) -> int:
        freqs = defaultdict(int)
        left = 0
        total_count = 0

        for right in range(len(nums)):
            freqs[nums[right]] += 1

            while len(freqs) > distinctK:
                freqs[nums[left]] -= 1
                if freqs[nums[left]] == 0:
                    del freqs[nums[left]]
                left += 1

            total_count += right - left + 1

        return total_count


# @lc code=end
