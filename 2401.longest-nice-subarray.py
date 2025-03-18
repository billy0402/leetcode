#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#

# @lc code=start
class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        max_length = 0
        used_bits = 0
        l = 0

        for r in range(len(nums)):
            while used_bits & nums[r] != 0:  # sliding windows
                used_bits ^= nums[l]  # remove left bits
                l += 1

            used_bits |= nums[r]
            max_length = max(max_length, r - l + 1)

        return max_length


# @lc code=end
