#
# @lc app=leetcode id=2116 lang=python3
#
# [2116] Check if a Parentheses String Can Be Valid
#

# @lc code=start
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False

        open_brackets: list[int] = []
        unlocked: list[int] = []

        for i in range(len(s)):
            char, is_locked = s[i], locked[i]
            if is_locked == "0":
                unlocked.append(i)
            elif char == "(":
                open_brackets.append(i)
            else:  # char == ')'  # noqa: PLR5501
                if open_brackets:
                    open_brackets.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        while open_brackets and unlocked and open_brackets[-1] < unlocked[-1]:
            open_brackets.pop()
            unlocked.pop()

        return not open_brackets
        # @lc code=end
