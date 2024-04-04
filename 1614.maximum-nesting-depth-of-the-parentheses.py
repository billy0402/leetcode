#
# @lc app=leetcode id=1614 lang=python3
#
# [1614] Maximum Nesting Depth of the Parentheses
#


# @lc code=start
class Solution:
    def maxDepth(self, s: str) -> int:
        counter = 0
        max_depth = 0

        for char in s:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
            max_depth = max(max_depth, counter)

        return max_depth


# @lc code=end
