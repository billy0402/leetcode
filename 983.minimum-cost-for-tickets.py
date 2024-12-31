#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#

# @lc code=start
class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp: dict[int, int] = {}

        def dfs(i: int) -> int:
            if i == len(days):
                return 0
            if i in dp:
                return dp[i]

            dp[i] = float("inf")  # pyright: ignore[reportArgumentType]
            for d, c in zip([1, 7, 30], costs, strict=True):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dfs(j))
            return dp[i]

        return dfs(0)


# @lc code=end
