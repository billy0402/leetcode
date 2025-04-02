#
# @lc app=leetcode id=2873 lang=python3
#
# [2873] Maximum Value of an Ordered Triplet I
#

# @lc code=start
class Solution:
    def maximumTripletValue(self, nums: list[int]) -> int:
        n = len(nums)
        result, i = 0, 0

        for j in range(1, n):
            if nums[j] > nums[i]:
                i = j
                continue

            for k in range(j + 1, n):
                result = max(result, (nums[i] - nums[j]) * nums[k])

        return result


# @lc code=end
