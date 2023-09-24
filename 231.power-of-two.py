#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#


# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        copy = n
        counter = 1
        while copy > 2:
            copy //= 2
            counter += 1
        return n == 2**counter


# @lc code=end
