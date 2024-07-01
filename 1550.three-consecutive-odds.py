#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
CONSECUTIVE_LENGTH = 3


class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        counter = 0
        for n in arr:
            if n % 2 == 0:
                counter = 0
                continue

            counter += 1
            if counter == CONSECUTIVE_LENGTH:
                return True
        return False


# @lc code=end
