#
# @lc app=leetcode id=1304 lang=python3
#
# [1304] Find N Unique Integers Sum up to Zero
#

# @lc code=start
class Solution:
    def sumZero(self, n: int) -> list[int]:
        results: list[int] = []

        for i in range(1, n // 2 + 1):
            results.append(i)
            results.append(-i)

        if n % 2 != 0:
            results.append(0)

        return results


# @lc code=end
