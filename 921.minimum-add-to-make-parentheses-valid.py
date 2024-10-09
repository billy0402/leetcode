#
# @lc app=leetcode id=921 lang=python3
#
# [921] Minimum Add to Make Parentheses Valid
#

# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        left_brackets = 0
        adds_required = 0

        for char in s:
            if char == "(":
                left_brackets += 1
            elif left_brackets:
                left_brackets -= 1
            else:
                adds_required += 1

        return left_brackets + adds_required


# @lc code=end
