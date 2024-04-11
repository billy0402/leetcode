#
# @lc app=leetcode id=402 lang=python3
#
# [402] Remove K Digits
#


# @lc code=start
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack: list[str] = []

        for n in num:
            while k > 0 and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            if stack or n != '0':
                stack.append(n)

        if k > 0:
            stack = stack[:-k]

        return ''.join(stack) or '0'


# @lc code=end
