#
# @lc app=leetcode id=2683 lang=python3
#
# [2683] Neighboring Bitwise XOR
#

# @lc code=start
class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        first = last = 0
        for n in derived:
            if n == 1:
                last = ~last
        return last == first


# @lc code=end
