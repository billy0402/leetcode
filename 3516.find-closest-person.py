#
# @lc app=leetcode id=3516 lang=python3
#
# [3516] Find Closest Person
#

# @lc code=start
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dxz, dyz = abs(x - z), abs(y - z)
        if dxz < dyz:
            return 1
        if dxz > dyz:
            return 2
        return 0


# @lc code=end
