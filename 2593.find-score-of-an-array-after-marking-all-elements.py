#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
import heapq


class Solution:
    def findScore(self, nums: list[int]) -> int:
        score = 0
        marked: set[int] = set()

        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)

        while heap:
            n, i = heapq.heappop(heap)
            if i in marked:
                continue

            score += n
            marked.add(i)
            marked.add(i - 1)
            marked.add(i + 1)

        return score


# @lc code=end
