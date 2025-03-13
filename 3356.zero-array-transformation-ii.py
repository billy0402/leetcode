#
# @lc app=leetcode id=3356 lang=python3
#
# [3356] Zero Array Transformation II
#

# @lc code=start
class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(queries)

        if not self._is_zero_array(nums, queries, n):
            return -1

        return self._binary_search(nums, queries)

    def _binary_search(self, nums: list[int], queries: list[list[int]]) -> int:
        left, right = 0, len(queries) - 1
        while left <= right:
            middle = (left + right) // 2
            if self._is_zero_array(nums, queries, middle):
                right = middle - 1
            else:
                left = middle + 1
        return left

    def _is_zero_array(self, nums: list[int], queries: list[list[int]], k: int) -> bool:
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for i in range(k):
            l, r, val = queries[i]

            prefix_sums[l] += val
            prefix_sums[r + 1] -= val

        total = 0
        for i in range(n):
            total += prefix_sums[i]
            if total < nums[i]:
                return False
        return True


# @lc code=end
