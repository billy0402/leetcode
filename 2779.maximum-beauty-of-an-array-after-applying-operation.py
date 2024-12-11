#
# @lc app=leetcode id=2779 lang=python3
#
# [2779] Maximum Beauty of an Array After Applying Operation
#

# @lc code=start
class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()

        max_beauty = 0
        l = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > k * 2:
                l += 1
            max_beauty = max(max_beauty, r - l + 1)
        return max_beauty


# @lc code=end
