#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        n = len(s)
        results: list[str] = []
        i = 0

        while i < n:
            results.append(s[i : i + k])
            i += k

        results[-1] += fill * (k - len(results[-1]))

        return results


# @lc code=end
