#
# @lc app=leetcode id=2395 lang=python3
#
# [2395] Find Subarrays With Equal Sum
#


# @lc code=start
class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        n = len(nums)
        totals = set()

        for i in range(n - 1):
            total = nums[i] + nums[i + 1]

            if total in totals:
                return True

            totals.add(total)

        return False


# @lc code=end
