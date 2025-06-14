#
# @lc app=leetcode id=3423 lang=python3
#
# [3423] Maximum Difference Between Adjacent Elements in a Circular Array
#

# @lc code=start
class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        result = abs(nums[len(nums) - 1] - nums[0])
        for i in range(len(nums) - 1):
            n1, n2 = nums[i], nums[i + 1]
            result = max(result, abs(n1 - n2))
        return result


# @lc code=end
