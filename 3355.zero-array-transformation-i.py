#
# @lc app=leetcode id=3355 lang=python3
#
# [3355] Zero Array Transformation I
#

# @lc code=start
class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        n = len(nums)
        prefix_sums = [0] * (n + 1)

        for l, r in queries:
            prefix_sums[l] += 1
            prefix_sums[r + 1] -= 1

        for i in range(1, n + 1):
            prefix_sums[i] += prefix_sums[i - 1]

        return all(prefix_sums[i] >= nums[i] for i in range(n))


# @lc code=end
