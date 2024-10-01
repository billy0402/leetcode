#
# @lc app=leetcode id=1497 lang=python3
#
# [1497] Check If Array Pairs Are Divisible by k
#

# @lc code=start
from collections import defaultdict


class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        freq: dict[int, int] = defaultdict(int)
        for n in arr:
            remainder = ((n % k) + k) % k
            freq[remainder] += 1

        if freq[0] % 2 != 0:
            return False

        return all(freq[i] == freq[k - i] for i in range(1, k // 2 + 1))


# @lc code=end
