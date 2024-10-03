#
# @lc app=leetcode id=1590 lang=python3
#
# [1590] Make Sum Divisible by P
#

# @lc code=start
class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        result = len(nums)
        current_sum = 0
        remain_to_index = {0: -1}
        for i, n in enumerate(nums):
            current_sum = (current_sum + n) % p
            prefix = (current_sum - remain + p) % p
            if prefix in remain_to_index:
                length = i - remain_to_index[prefix]
                result = min(length, result)
            remain_to_index[current_sum] = i

        return result if result != len(nums) else -1


# @lc code=end
