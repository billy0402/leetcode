#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        target, remainder = divmod(total, 2)
        if remainder != 0:
            return False

        cache = {0}

        for i in range(len(nums) - 1, -1, -1):
            current_cache = cache.copy()

            for previous_sum in current_cache:
                cache.add(previous_sum + nums[i])
                cache.add(previous_sum)

        return target in cache


# @lc code=end
