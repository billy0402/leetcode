#
# @lc app=leetcode id=1190 lang=python3
#
# [1190] Reverse Substrings Between Each Pair of Parentheses
#

# @lc code=start
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_parentheses_indices: list[int] = []
        pair = [-1] * n

        for i in range(n):
            if s[i] == "(":
                open_parentheses_indices.append(i)
            elif s[i] == ")":
                j = open_parentheses_indices.pop()
                pair[i] = j
                pair[j] = i

        result: list[str] = []
        index, step = 0, 1

        while index < n:
            if s[index] == "(" or s[index] == ")":
                index = pair[index]
                step = -step
            else:
                result.append(s[index])
            index += step

        return "".join(result)


# @lc code=end
