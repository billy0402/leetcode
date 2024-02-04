#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#

# @lc code=start
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        sub_length = gcd(len(str1), gcd(len(str2)))
        return str1[:sub_length]


# @lc code=end
