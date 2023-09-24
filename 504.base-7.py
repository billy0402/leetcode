#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#


# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ''
        n = abs(num)

        if n < 7:
            result = str(n)

        while n >= 7:
            n, mod = divmod(n, 7)
            result += str(mod)

            if n < 7:
                result += str(n)

        result = result[::-1]

        if num < 0:
            result = f'-{result}'
        return result


# @lc code=end
