#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        counter = 0
        n = len(nums)
        distinct = len(set(nums))
        freq: dict[int, int] = defaultdict(int)
        right = 0

        for left in range(n):
            if left > 0:
                remove = nums[left - 1]
                freq[remove] -= 1
                if freq[remove] == 0:
                    del freq[remove]

            while right < n and len(freq) < distinct:
                add = nums[right]
                freq[add] += 1
                right += 1

            if len(freq) == distinct:
                counter += n - right + 1

        return counter


# @lc code=end
