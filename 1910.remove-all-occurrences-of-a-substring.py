#
# @lc app=leetcode id=1910 lang=python3
#
# [1910] Remove All Occurrences of a Substring
#

# @lc code=start
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack: list[str] = []
        part_n = len(part)

        for char in s:
            stack.append(char)

            while len(stack) >= part_n and "".join(stack[-part_n:]) == part:
                for _ in part:
                    stack.pop()

        return "".join(stack)


# @lc code=end
