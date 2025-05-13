#
# @lc app=leetcode id=2094 lang=python3
#
# [2094] Finding 3-Digit Even Numbers
#

# @lc code=start
from collections import Counter


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        results: list[int] = []
        freq = Counter(digits)

        for n in range(100, 1000, 2):
            i, j, k = n // 100, n // 10 % 10, n % 10
            counter = Counter((i, j, k))
            if all(freq[num] >= count for num, count in counter.items()):
                results.append(n)

        return results


# @lc code=end
