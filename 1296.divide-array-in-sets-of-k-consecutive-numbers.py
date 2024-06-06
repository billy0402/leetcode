#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#

# @lc code=start
from collections import Counter


class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        counter = Counter(nums)

        for _ in range(0, len(nums), k):
            min_n = min(counter)

            for i in range(k):
                n = min_n + i
                if n not in counter:
                    return False

                counter[n] -= 1
                if counter[n] == 0:
                    del counter[n]

        return True


# @lc code=end
