#
# @lc app=leetcode id=3075 lang=python3
#
# [3075] Maximize Happiness of Selected Children
#

# @lc code=start
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse=True)

        total_happiness = 0

        for i in range(k):
            # use max function prevent negative
            total_happiness += max(happiness[i] - i, 0)

        return total_happiness


# @lc code=end
