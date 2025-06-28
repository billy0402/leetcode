#
# @lc app=leetcode id=2099 lang=python3
#
# [2099] Find Subsequence of Length K With the Largest Sum
#

# @lc code=start
import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        largest: list[tuple[int, int]] = []
        for i, n in enumerate(nums):
            if len(largest) < k:
                heapq.heappush(largest, (n, i))
            else:
                heapq.heappushpop(largest, (n, i))

        largest.sort(key=lambda x: x[1])

        return [n for n, _ in largest]


# @lc code=end
