#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        counter = 0

        for i in range(low, high + 1):
            s = str(i)
            half, remainder = divmod(len(s), 2)
            if remainder:
                continue

            left = sum(int(x) for x in s[:half])
            right = sum(int(x) for x in s[half:])
            if left == right:
                counter += 1

        return counter


# @lc code=end
