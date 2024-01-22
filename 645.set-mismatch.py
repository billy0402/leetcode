#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#


# @lc code=start
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        actual_sum = sum(nums)
        unique_sum = sum(set(nums))
        except_nums = n * (n + 1) // 2
        duplicate = actual_sum - unique_sum
        missing = except_nums - unique_sum
        return [duplicate, missing]


# @lc code=end
