#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#


# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        total = 0
        for n in range(1, int(num**0.5) + 1):
            if num % n == 0:
                total += n
                if n * n != num:
                    total += num // n
        return total == num * 2


# @lc code=end
