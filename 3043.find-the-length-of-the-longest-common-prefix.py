#
# @lc app=leetcode id=3043 lang=python3
#
# [3043] Find the Length of the Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        arr1_prefixes: set[int] = set()
        for num in arr1:
            value = num
            while value > 0 and value not in arr1_prefixes:
                arr1_prefixes.add(value)
                value //= 10

        longest_prefix = 0
        for num in arr2:
            value = num
            while value > 0 and value not in arr1_prefixes:
                value //= 10
            if value in arr1_prefixes:
                longest_prefix = max(len(str(value)), longest_prefix)
        return longest_prefix


# @lc code=end
