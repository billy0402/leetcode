#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#

# @lc code=start
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(current: int) -> int:
            result = 0
            neighbor = current + 1

            while current <= n:
                result += min(neighbor, n + 1) - current
                current *= 10
                neighbor *= 10

            return result

        current = 1
        i = 1

        while i < k:
            steps = count(current)

            if i + steps <= k:
                current += 1
                i += steps
            else:
                current *= 10
                i += 1

        return current


# @lc code=end
