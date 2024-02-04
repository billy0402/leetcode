#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#


# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        start = 1
        # 1 = 1 ~ 9
        # 2 = 10 ~ 99
        # 3 = 100 ~ 999
        length = 1
        # 9   = 9 - 1 + 1
        # 90  = 99 - 10 + 1
        # 900 = 999 - 100 + 1
        count = 9

        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        i, j = divmod(n - 1, length)

        return int(str(start + i)[j])


# @lc code=end
