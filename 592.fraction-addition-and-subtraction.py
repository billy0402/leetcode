#
# @lc app=leetcode id=592 lang=python3
#
# [592] Fraction Addition and Subtraction
#

# @lc code=start
import re
from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1

        nums = re.findall(r"[+-]?\d+", expression)

        for i in range(0, len(nums), 2):
            cur_num = int(nums[i])
            cur_denom = int(nums[i + 1])

            numerator = numerator * cur_denom + cur_num * denominator
            denominator *= cur_denom

        common_divisor = gcd(abs(numerator), denominator)
        numerator //= common_divisor
        denominator //= common_divisor

        return f"{numerator}/{denominator}"


# @lc code=end
