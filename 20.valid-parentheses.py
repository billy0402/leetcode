#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
from typing import List

d = {
    '(': ')',
    '[': ']',
    '{': '}',
}


class Solution:
    def isValid(self, s: str) -> bool:
        stack: List[str] = []
        for bracket in s:
            if bracket in d:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != d[stack.pop()]:
                return False

        return len(stack) == 0


# @lc code=end
