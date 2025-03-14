#
# @lc app=leetcode id=2226 lang=python3
#
# [2226] Maximum Candies Allocated to K Children
#

# @lc code=start
class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0
        return self._binary_search(candies, k)

    def _binary_search(self, candies: list[int], k: int) -> int:
        left, right = 1, sum(candies) // k
        while left <= right:
            middle = (left + right) // 2
            if self._can_allocate(candies, k, middle):
                left = middle + 1
            else:
                right = middle - 1
        return right

    def _can_allocate(self, candies: list[int], k: int, n: int) -> bool:
        piles = 0
        for candy in candies:
            piles += candy // n
            if piles >= k:
                return True
        return False


# @lc code=end
