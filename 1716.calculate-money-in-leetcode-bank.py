#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
WEEK_TOTAL = (1 + 7) * 7 // 2


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, extra = divmod(n, 7)
        results = WEEK_TOTAL * weeks
        results += 7 * weeks * (weeks - 1) // 2
        results += ((weeks + 1) + (weeks + extra)) * extra // 2
        return results


# @lc code=end
