#
# @lc app=leetcode id=1399 lang=python3
#
# [1399] Count Largest Group
#

# @lc code=start
from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups: dict[int, int] = defaultdict(int)
        for digits in range(1, n + 1):
            copy, total = digits, 0
            while copy:
                copy, remainder = divmod(copy, 10)
                total += remainder
            groups[total] += 1

        counter, largest_size = 0, 0
        for size in groups.values():
            if size > largest_size:
                counter, largest_size = 1, size
            elif size == largest_size:
                counter += 1
        return counter


# @lc code=end
