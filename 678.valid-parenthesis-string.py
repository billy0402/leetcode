#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#


# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_brackets: list[int] = []
        asterisks: list[int] = []

        for i, char in enumerate(s):
            if char == '(':
                open_brackets.append(i)
            elif char == '*':
                asterisks.append(i)
            else:  # char == ')'
                if open_brackets:
                    open_brackets.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False

        while open_brackets and asterisks:
            if open_brackets.pop() > asterisks.pop():
                return False

        return not open_brackets


# @lc code=end
