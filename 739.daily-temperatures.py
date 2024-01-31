#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#


# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        results = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            t = temperatures[i]

            while stack and t >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                results[i] = stack[-1] - i

            stack.append(i)

        return results


# @lc code=end
