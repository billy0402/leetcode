#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
MAX_SUB_LENGTH = 2


class Solution:
    def makeFancyString(self, s: str) -> str:
        results: list[str] = []
        for char in s:
            if len(results) >= MAX_SUB_LENGTH and results[-2] == results[-1] == char:
                continue
            results.append(char)
        return "".join(results)


# @lc code=end
