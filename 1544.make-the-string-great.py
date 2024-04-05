#
# @lc app=leetcode id=1544 lang=python3
#
# [1544] Make The String Great
#


# @lc code=start
class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []

        for char in s:
            if stack and abs(ord(char) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)


# @lc code=end
