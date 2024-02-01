#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#


# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        answer = 0
        buy = float('inf')

        for sell in prices:
            if sell > buy:
                answer = max(answer, sell - buy)
            else:
                buy = sell

        return answer


# @lc code=end
