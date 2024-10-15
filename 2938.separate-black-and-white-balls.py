#
# @lc app=leetcode id=2938 lang=python3
#
# [2938] Separate Black and White Balls
#

# @lc code=start
WHITE = "0"
BLACK = "1"


class Solution:
    def minimumSteps(self, s: str) -> int:
        total_swaps = 0
        black_counter = 0

        for char in s:
            if char == WHITE:
                total_swaps += black_counter
            else:
                black_counter += 1

        return total_swaps


# @lc code=end
