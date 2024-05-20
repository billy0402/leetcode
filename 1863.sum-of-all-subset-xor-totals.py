#
# @lc app=leetcode id=1863 lang=python3
#
# [1863] Sum of All Subset XOR Totals
#

# @lc code=start
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def backtracking(current: list[int], index: int):
            if index == len(nums):
                subsets.append(current[:])
                return

            # generate subset include nums[index]
            current.append(nums[index])
            backtracking(current, index + 1)
            current.pop()

            # generate subset exclude nums[index]
            backtracking(current, index + 1)

        subsets: list[list[int]] = []
        backtracking([], 0)

        total = 0
        for subset in subsets:
            xor = 0
            for num in subset:
                xor ^= num
            total += xor
        return total


# @lc code=end
