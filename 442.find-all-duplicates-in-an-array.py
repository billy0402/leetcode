#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#


# @lc code=start
class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        results: list[int] = []
        for n in nums:
            n = abs(n)
            if nums[n - 1] < 0:
                results.append(n)
            nums[n - 1] *= -1
        return results


# @lc code=end
