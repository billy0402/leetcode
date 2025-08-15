#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return n.bit_count() == 1 and n.bit_length() % 2 == 1


# @lc code=end
