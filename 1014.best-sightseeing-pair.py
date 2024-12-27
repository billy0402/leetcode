#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        max_score = 0
        max_i_value = values[0]  # values[i] + i in index 0

        for j in range(1, len(values)):
            max_score = max(max_score, max_i_value + values[j] - j)
            max_i_value = max(max_i_value, values[j] + j)

        return max_score


# @lc code=end
