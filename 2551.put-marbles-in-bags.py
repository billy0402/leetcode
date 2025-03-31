#
# @lc app=leetcode id=2551 lang=python3
#
# [2551] Put Marbles in Bags
#

# @lc code=start
class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        pair_weights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        pair_weights.sort()

        n = len(pair_weights)
        diff_score = 0
        for i in range(k - 1):
            diff_score += pair_weights[n - 1 - i] - pair_weights[i]
        return diff_score


# @lc code=end
