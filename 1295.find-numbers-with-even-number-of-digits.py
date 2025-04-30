#
# @lc app=leetcode id=1295 lang=python3
#
# [1295] Find Numbers with Even Number of Digits
#

# @lc code=start
import math


class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        counter = 0

        for n in nums:
            digit_count = int(math.floor(math.log10(n))) + 1
            if digit_count % 2 == 0:
                counter += 1

        return counter


# @lc code=end
