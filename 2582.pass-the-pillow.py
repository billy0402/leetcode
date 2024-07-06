#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        turn, index = divmod(time, n - 1)

        if turn % 2 == 0:
            return index + 1
        return n - index


# @lc code=end
