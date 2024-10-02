#
# @lc app=leetcode id=1331 lang=python3
#
# [1331] Rank Transform of an Array
#

# @lc code=start
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_arr = sorted(set(arr))
        ranks = {n: i + 1 for i, n in enumerate(sorted_arr)}
        return [ranks[n] for n in arr]


# @lc code=end
