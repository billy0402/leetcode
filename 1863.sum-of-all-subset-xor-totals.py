#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtracking(i: int, total: int) -> int:
            if i == len(nums):
                return total

            # generate subset include nums[index]
            include_i = backtracking(i + 1, total ^ nums[i])
            # generate subset exclude nums[index]
            exclude_i = backtracking(i + 1, total)
            return include_i + exclude_i

        return backtracking(0, 0)


# @lc code=end
