#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#


# @lc code=start
class Solution:
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums):
            if not minK <= num <= maxK:
                bad_idx = i

            if num == minK:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res


# @lc code=end
