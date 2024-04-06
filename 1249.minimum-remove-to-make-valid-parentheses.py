#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack: deque[str] = deque()
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    continue
                stack.append(i)

        result: list[str] = []
        for i, char in enumerate(s):
            if stack and i == stack[0]:
                stack.popleft()
                continue
            result.append(char)

        return ''.join(result)


# @lc code=end
