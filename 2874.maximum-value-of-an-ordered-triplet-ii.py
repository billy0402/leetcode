#
# @lc app=leetcode id=2874 lang=python3
#
# [2874] Maximum Value of an Ordered Triplet II
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        result, max_prefix, max_diff = 0, 0, 0

        for k in nums:
            result = max(result, max_diff * k)
            max_prefix = max(max_prefix, k)
            max_diff = max(max_diff, max_prefix - k)

        return result


# @lc code=end
