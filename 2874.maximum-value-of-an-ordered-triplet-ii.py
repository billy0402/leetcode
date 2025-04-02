#
# @lc app=leetcode id=2874 lang=python3
#
# [2874] Maximum Value of an Ordered Triplet II
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_max = [0] * n
        suffix_max = [0] * n
        for i in range(1, n):
            prefix_max[i] = max(nums[i - 1], prefix_max[i - 1])
            suffix_max[n - 1 - i] = max(nums[n - i], suffix_max[n - i])

        result = 0
        for i in range(1, n - 1):
            result = max(result, (prefix_max[i] - nums[i]) * suffix_max[i])
        return result


# @lc code=end
