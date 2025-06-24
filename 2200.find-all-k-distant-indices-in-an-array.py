#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        results: list[int] = []
        r = 0

        for i, n in enumerate(nums):
            if n != key:
                continue

            l = max(r, i - k)  # noqa: E741
            r = min(len(nums) - 1, i + k) + 1
            results.extend(range(l, r))

        return results


# @lc code=end
