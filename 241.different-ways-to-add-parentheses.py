#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        results: list[int] = []

        for index, char in enumerate(expression):
            if char.isdigit():
                continue

            left = self.diffWaysToCompute(expression[0:index])
            right = self.diffWaysToCompute(expression[index + 1 :])

            for i in left:
                for j in right:
                    if char == "+":
                        results.append(int(i) + int(j))
                    elif char == "-":
                        results.append(int(i) - int(j))
                    elif char == "*":
                        results.append(int(i) * int(j))

        if len(results) == 0:
            results.append(int(expression))

        return results


# @lc code=end
