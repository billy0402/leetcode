#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        answers: list[int] = []
        temp = 0

        if len(num2) > len(num1):
            num1, num2 = num2, num1

        for i in range(-1, -len(num1) - 1, -1):
            n1 = int(num1[i])
            n2 = int(num2[i]) if i > -len(num2) - 1 else 0
            temp, n = divmod(n1 + n2 + temp, 10)
            answers.append(str(n))
        if temp != 0:
            answers.append(str(temp))

        return ''.join(reversed(answers))


# @lc code=end
