#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#


# @lc code=start
class Solution:
    """
    5：1|01
    7：1|11
         ^ 從這裡開始不一樣
    所以答案是：
    4：1|00
    """
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        zeros = 0
        while left != right:
            left >>= 1
            right >>= 1
            zeros += 1
        return left << zeros


# @lc code=end
