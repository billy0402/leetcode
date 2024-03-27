#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#


# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        left = 0
        counter = 0
        product = 1

        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            counter += (right - left + 1)

        return counter


# @lc code=end
