#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#


# @lc code=start
class Solution:
    hash_table: dict[int, int]

    def __init__(self):
        self.hash_table = {0: 0, 1: 1}

    def fib(self, n: int) -> int:
        if self.hash_table.get(n) is not None:
            return self.hash_table[n]

        self.hash_table[n] = self.fib(n - 1) + self.fib(n - 2)
        return self.hash_table[n]


# @lc code=end
