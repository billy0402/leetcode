#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        for i, c in enumerate(s):
            if (i + 1 != len(s)) and (d[s[i + 1]] > d[c]):
                total -= d[c]
            else:
                total += d[c]

        return total


# @lc code=end
