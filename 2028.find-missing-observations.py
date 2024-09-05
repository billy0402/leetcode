#
# @lc app=leetcode id=2028 lang=python3
#
# [2028] Find Missing Observations
#

# @lc code=start
DICE_MIN = 1
DICE_MAX = 6


class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        total_sum = mean * (len(rolls) + n)
        known_sum = sum(rolls)
        unknown_sum = total_sum - known_sum

        if not (DICE_MIN <= unknown_sum / n <= DICE_MAX):
            return []

        unknown_mean, mod = divmod(unknown_sum, n)
        result = [unknown_mean] * n
        for i in range(mod):
            result[i] += 1

        return result


# @lc code=end
