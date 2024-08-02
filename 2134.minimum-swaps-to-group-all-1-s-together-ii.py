#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        max_ones = current_ones = 0
        l = 0

        for r in range(n * 2):
            if nums[r % n] == 1:
                current_ones += 1

            if r - l + 1 > total_ones:
                current_ones -= nums[l % n]
                l += 1

            max_ones = max(max_ones, current_ones)

        return total_ones - max_ones


# @lc code=end
