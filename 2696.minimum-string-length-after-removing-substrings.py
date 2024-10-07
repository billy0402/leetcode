#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:
        stack: list[str] = []

        for char in s:
            if not stack:
                stack.append(char)
            elif char == "B" and stack[-1] == "A" or char == "D" and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(char)

        return len(stack)


# @lc code=end
