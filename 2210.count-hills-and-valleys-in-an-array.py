#
# @lc app=leetcode id=2210 lang=python3
#
# [2210] Count Hills and Valleys in an Array
#

# @lc code=start
class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        prev, count = nums[0], 0
        for i in range(1, len(nums) - 1):
            current, next_ = nums[i], nums[i + 1]
            if current == next_:  # same hill or valley
                continue
            if (
                current > prev and current > next_  # hill
            ) or (
                current < prev and current < next_  # valley
            ):
                count += 1
            prev = nums[i]
        return count


# @lc code=end
