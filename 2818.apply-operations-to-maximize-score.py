#
# @lc app=leetcode id=2818 lang=python3
#
# [2818] Apply Operations to Maximize Score
#

# @lc code=start
import math
from heapq import heapify, heappop

MOD = 10**9 + 7


class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        n = len(nums)
        result = 1

        prime_scores: list[int] = []
        for num in nums:
            score = 0
            for f in range(2, int(math.sqrt(num)) + 1):
                if num % f == 0:
                    score += 1
                    while num % f == 0:
                        num //= f  # noqa: PLW2901

            if num >= 2:  # noqa: PLR2004
                score += 1

            prime_scores.append(score)

        left_bound = [-1] * n
        right_bound = [n] * n

        stack: list[int] = []  # indexes of decreasing or equal order scores
        for i, score in enumerate(prime_scores):
            while stack and prime_scores[stack[-1]] < score:
                index = stack.pop()
                right_bound[index] = i

            if stack:
                left_bound[i] = stack[-1]

            stack.append(i)

        min_heap: list[tuple[int, int]] = [(-num, i) for i, num in enumerate(nums)]
        heapify(min_heap)

        while k > 0:
            num, i = heappop(min_heap)
            num = -num
            score = prime_scores[i]

            left_count = i - left_bound[i]
            right_count = right_bound[i] - i

            count = left_count * right_count
            operations = min(count, k)
            result = (result * pow(num, operations, MOD)) % MOD
            k -= operations

        return result


# @lc code=end
