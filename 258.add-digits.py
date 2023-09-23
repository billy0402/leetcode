#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#


# @lc code=start
class Solution:
    @staticmethod
    def sum(num: int):
        s = str(num)

        total = 0
        for n in s:
            total += int(n)

        return total

    def addDigits(self, num: int) -> int:
        total = self.sum(num)
        while total >= 10:
            total = self.sum(total)
        return total


# @lc code=end
