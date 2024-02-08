#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        coins.sort()

        for target in range(1, amount + 1):
            for coin in coins:
                if target < coin:
                    break
                dp[target] = min(dp[target], dp[target - coin] + 1)

        return dp[amount] if dp[amount] != amount + 1 else -1


# @lc code=end
