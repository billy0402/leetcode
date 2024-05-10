#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#

# @lc code=start
class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        fractions: list[tuple[int]] = []
        n = len(arr)

        for i in range(n):
            for j in range(i, n):
                fractions.append((arr[i], arr[j]))

        fractions.sort(key=lambda x: x[0] / x[1])

        return list(fractions[k - 1])


# @lc code=end
