#
# @lc app=leetcode id=2560 lang=python3
#
# [2560] House Robber IV
#

# @lc code=start
class Solution:
    def minCapability(self, nums: list[int], k: int) -> int:
        return self._binary_search(nums, k)

    def _binary_search(self, nums: list[int], k: int) -> int:
        left, right = min(nums), max(nums)
        while left <= right:
            middle = (left + right) // 2
            if self._is_valid(nums, k, middle):
                right = middle - 1
            else:
                left = middle + 1
        return right + 1

    def _is_valid(self, nums: list[int], k: int, capability: int) -> bool:
        i = count = 0
        while i < len(nums):
            if nums[i] <= capability:
                i += 2
                count += 1
            else:
                i += 1
            if count == k:
                break
        return count == k


# @lc code=end
