#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#

# @lc code=start
A = 65
Z = 90
a = 97


class Solution:
    def toLowerCase(self, s: str) -> str:
        results = []

        for c in s:
            if A <= ord(c) <= Z:
                lower = chr(ord(c) + (a - A))
                results.append(lower)
            else:
                results.append(c)

        return ''.join(results)


# @lc code=end
