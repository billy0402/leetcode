#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#

# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        results: list[int] = []
        current = 1

        while len(results) < n:
            results.append(current)

            if current * 10 <= n:
                current *= 10
            else:
                while current >= n or current % 10 == 9:
                    current //= 10
                current += 1

        return results


# @lc code=end
