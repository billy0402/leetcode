#
# @lc app=leetcode id=1475 lang=python3
#
# [1475] Final Prices With a Special Discount in a Shop
#

# @lc code=start
class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        answer = prices.copy()
        stack: list[int] = []  # the indexes that values are increasing order

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                j = stack.pop()
                answer[j] -= prices[i]

            stack.append(i)

        return answer


# @lc code=end
