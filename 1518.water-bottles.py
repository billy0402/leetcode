#
# @lc app=leetcode id=1518 lang=python3
#
# [1518] Water Bottles
#

# @lc code=start
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = 0
        empty = 0

        while numBottles:
            drank += numBottles
            empty += numBottles
            numBottles = 0

            exchange = empty // numExchange
            empty -= numExchange * exchange
            numBottles = exchange

        return drank


# @lc code=end
