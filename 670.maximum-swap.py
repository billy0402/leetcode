#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#

# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        max_i = swap_i = swap_j = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[max_i]:
                max_i = i

            if nums[i] < nums[max_i]:
                swap_i, swap_j = i, max_i

        nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]

        return int("".join(nums))


# @lc code=end
