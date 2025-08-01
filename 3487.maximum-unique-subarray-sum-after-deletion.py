#
# @lc app=leetcode id=3487 lang=python3
#
# [3487] Maximum Unique Subarray Sum After Deletion
#

# @lc code=start
class Solution:
    def maxSum(self, nums: list[int]) -> int:
        max_num = max(nums)
        return max_num if max_num < 0 else sum({n for n in nums if n > 0})


# @lc code=end
