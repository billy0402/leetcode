#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#


# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                substr: list[str] = []
                times: list[str] = []
                while stack[-1] != '[':
                    substr.append(stack.pop())
                stack.pop()  # '['
                while stack and stack[-1].isdigit():
                    times.append(stack.pop())

                s = ''.join(reversed(substr))
                n = int(''.join(reversed(times)))
                stack.append(s * n)

        return ''.join(stack)


# @lc code=end
