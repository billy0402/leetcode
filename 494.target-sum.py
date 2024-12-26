#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp: dict[tuple[int, int], int] = {}  # { (index, current_sum): ways }

        def backtracking(i: int, current_sum: int) -> int:
            if (i, current_sum) in dp:
                return dp[(i, current_sum)]

            if i == len(nums):
                return 1 if current_sum == target else 0

            n = nums[i]
            plus = backtracking(i + 1, current_sum + n)
            minus = backtracking(i + 1, current_sum - n)
            dp[(i, current_sum)] = plus + minus
            return dp[(i, current_sum)]

        return backtracking(0, 0)


# @lc code=end
