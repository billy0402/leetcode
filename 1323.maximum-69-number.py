#
# @lc app=leetcode id=1323 lang=python3
#
# [1323] Maximum 69 Number
#


# @lc code=start
class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)

        for i in range(len(s)):
            n = s[i]
            if n == '6':
                s = s[:i] + '9' + s[i + 1:]
                break

        return int(s)


# @lc code=end
