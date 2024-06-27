#
# @lc app=leetcode id=1791 lang=python3
#
# [1791] Find Center of Star Graph
#

# @lc code=start
class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        u0, v0 = edges[0]
        e1 = edges[1]

        if u0 in e1:
            return u0
        return v0


# @lc code=end
