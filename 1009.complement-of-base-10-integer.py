#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1

        bit_length = n.bit_length()
        mask = (1 << bit_length) - 1
        return n ^ mask


# @lc code=end
