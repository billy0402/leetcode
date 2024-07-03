#
# @lc app=leetcode id=1509 lang=python3
#
# [1509] Minimum Difference Between Largest and Smallest Value in Three Moves
#

# @lc code=start
import heapq


class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) <= 4:
            return 0

        min_four = sorted(heapq.nsmallest(4, nums))
        max_four = sorted(heapq.nlargest(4, nums))

        answer = float("inf")
        for l, r in zip(min_four, max_four, strict=True):
            answer = min(answer, r - l)
        return answer


# @lc code=end
