#
# @lc app=leetcode id=2337 lang=python3
#
# [2337] Move Pieces to Obtain a String
#

# @lc code=start
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(target)
        l = r = 0

        while l < n or r < n:
            while l < n and start[l] == "_":
                l += 1
            while r < n and target[r] == "_":
                r += 1

            if l == n or r == n:  # noqa: PLR1714
                return l == n and r == n

            s_c = start[l]
            t_c = target[r]
            if s_c != t_c or (s_c == "L" and l < r) or (s_c == "R" and l > r):
                return False

            l += 1
            r += 1

        return True


# @lc code=end
